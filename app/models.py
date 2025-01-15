from sqlalchemy import Enum, Date, Integer, TypeDecorator
from flask_sqlalchemy import SQLAlchemy

# Veritabanı bağlantısı
db = SQLAlchemy()

# Custom VARCHAR TypeDecorator
class VARCHAR(TypeDecorator):
    impl = db.String

    def __init__(self, length):
        self.length = length
        super().__init__()

# Membership Modeli
class Membership(db.Model):
    __tablename__ = 'membership'
    m_id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(Date)
    end_date = db.Column(Date)

    # Relationship
    customers = db.relationship('Customer', backref='membership', lazy=True)

# EmployeeDetails Modeli
class EmployeeDetails(db.Model):
    __tablename__ = 'employee_details'
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(VARCHAR(30))
    emp_designation = db.Column(VARCHAR(40))
    emp_addr = db.Column(VARCHAR(100))
    emp_branch = db.Column(VARCHAR(15))
    emp_cont_no = db.Column(db.Integer)

    # Relationship
    managed_shipments = db.relationship('EmployeeManagesShipment', backref='employee', lazy=True)

# Status Modeli
class Status(db.Model):
    __tablename__ = 'status'
    sh_id = db.Column(db.Integer, primary_key=True)
    current_st = db.Column(VARCHAR(15))
    sent_date = db.Column(Date)
    delivery_date = db.Column(Date)

    # Relationship
    managed_shipments = db.relationship('EmployeeManagesShipment', backref='status', lazy=True)

# ShipmentDetails Modeli
class ShipmentDetails(db.Model):
    __tablename__ = 'shipment_details'
    sd_id = db.Column(db.Integer, primary_key=True)
    customer_cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id'))
    sd_content = db.Column(VARCHAR(40))
    sd_domain = db.Column(Enum('International', 'Domestic', name='sd_domain_enum'))
    sd_type = db.Column(Enum('Express', 'Regular', name='sd_type_enum'))
    sd_weight = db.Column(VARCHAR(10))
    sd_charges = db.Column(db.Integer)
    sd_addr = db.Column(VARCHAR(100))
    ds_addr = db.Column(VARCHAR(100))

    # Relationship
    payments = db.relationship('PaymentDetails', backref='shipment', lazy=True)
    managed_shipments = db.relationship('EmployeeManagesShipment', backref='shipment', lazy=True)

# Customer Modeli
class Customer(db.Model):
    __tablename__ = 'customer'
    cust_id = db.Column(db.Integer, primary_key=True)
    membership_m_id = db.Column(db.Integer, db.ForeignKey('membership.m_id'))
    cust_name = db.Column(VARCHAR(30))
    cust_email = db.Column(VARCHAR(50))
    cust_type = db.Column(Enum('Wholesale', 'Retail', 'Internal Goods', name='cust_type_enum'))
    cust_addr = db.Column(VARCHAR(100))
    cust_cont_no = db.Column(db.Integer)

    # Relationship
    shipments = db.relationship('ShipmentDetails', backref='customer', lazy=True)

# PaymentDetails Modeli
class PaymentDetails(db.Model):
    __tablename__ = 'payment_details'
    payment_id = db.Column(VARCHAR(40), primary_key=True)
    shipment_client_c_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id'))
    shipment_sh_id = db.Column(db.Integer, db.ForeignKey('shipment_details.sd_id'))
    amount = db.Column(db.Integer)
    payment_status = db.Column(Enum('PAID', 'NOT PAID', name='payment_status_enum'))
    payment_mode = db.Column(Enum('COD', 'CARD PAYMENT', name='payment_mode_enum'))
    payment_date = db.Column(db.Date)

# Employee Manages Shipment Modeli
class EmployeeManagesShipment(db.Model):
    __tablename__ = 'employee_manages_shipment'
    
    # Foreign key sütunları
    employee_e_id = db.Column(db.Integer, db.ForeignKey('employee_details.emp_id'), primary_key=True)
    shipment_sh_id = db.Column(db.Integer, db.ForeignKey('shipment_details.sd_id'), primary_key=True)
    status_sh_id = db.Column(db.Integer, db.ForeignKey('status.sh_id'), primary_key=True)

    # İlişkiler
    employee = db.relationship('EmployeeDetails', backref=db.backref('shipments_managed', lazy=True))
    shipment = db.relationship('ShipmentDetails', backref=db.backref('managed_by_employees', lazy=True))
    status = db.relationship('Status', backref=db.backref('assigned_to_shipments', lazy=True))

    # Location Modeli
class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(VARCHAR(100), nullable=False)
    country = db.Column(VARCHAR(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "city": self.city, "country": self.country}

# Route Modeli
class Route(db.Model):
    __tablename__ = 'routes'
    id = db.Column(db.Integer, primary_key=True)
    start_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    end_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    distance = db.Column(db.Integer, nullable=False)

    # Relationships
    start_location = db.relationship('Location', foreign_keys=[start_location_id], backref='start_routes')
    end_location = db.relationship('Location', foreign_keys=[end_location_id], backref='end_routes')

    def to_dict(self):
        return {
            "id": self.id,
            "start_location": self.start_location.city,
            "end_location": self.end_location.city,
            "distance": self.distance
        }

# User Modeli (Gönderici, Alıcı, Kurye)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(VARCHAR(100), nullable=False)
    user_type = db.Column(VARCHAR(50), nullable=False)  # 'Sender', 'Receiver', 'Courier'

    def to_dict(self):
        return {"id": self.id, "name": self.name, "user_type": self.user_type}

# Delivery Modeli
class Delivery(db.Model):
    __tablename__ = 'deliveries'
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    courier_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(VARCHAR(50), nullable=False)  # 'Completed', 'Cancelled', 'Delayed'
    estimated_time = db.Column(db.Interval, nullable=False)

    # Relationships
    route = db.relationship('Route', backref=db.backref('deliveries', lazy=True))
    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_deliveries')
    receiver = db.relationship('User', foreign_keys=[receiver_id], backref='received_deliveries')
    courier = db.relationship('User', foreign_keys=[courier_id], backref='managed_deliveries')

    def to_dict(self):
        return {
            "id": self.id,
            "route": self.route.to_dict(),
            "sender": self.sender.name,
            "receiver": self.receiver.name,
            "courier": self.courier.name,
            "status": self.status,
            "estimated_time": str(self.estimated_time)
        }