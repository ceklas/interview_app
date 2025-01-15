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

# EmployeeDetails Modeli
class EmployeeDetails(db.Model):
    __tablename__ = 'employee_details'
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(VARCHAR(30))
    emp_designation = db.Column(VARCHAR(40))
    emp_addr = db.Column(VARCHAR(100))
    emp_branch = db.Column(VARCHAR(15))
    emp_cont_no = db.Column(db.Integer)  

# Status Modeli
class Status(db.Model):
    __tablename__ = 'status'
    sh_id = db.Column(db.Integer, primary_key=True)
    current_st = db.Column(VARCHAR(15))
    sent_date = db.Column(Date)
    delivery_date = db.Column(Date)

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

# PaymentDetails Modeli
class PaymentDetails(db.Model):
    __tablename__ = 'payment_details'
    payment_id = db.Column(VARCHAR(40), primary_key=True)
    shipment_client_c_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id'))
    shipment_sh_id = db.Column(db.Integer, db.ForeignKey('shipment_details.sd_id'))
    amount = db.Column(db.Integer)
    payment_status = db.Column(Enum('Paid', 'Not Paid', name='payment_status_enum'))
    payment_mode = db.Column(Enum('COD', 'Card Payment', name='payment_mode_enum'))
    payment_date = db.Column(db.Date) 

# Employee Manages Shipment Modeli
class EmployeeManagesShipment(db.Model):
    __tablename__ = 'employee_manages_shipment'
    employee_e_id = db.Column(db.Integer, db.ForeignKey('employee_details.emp_id'), primary_key=True)
    shipment_sh_id = db.Column(db.Integer, db.ForeignKey('shipment_details.sd_id'), primary_key=True)
    status_sh_id = db.Column(db.Integer, db.ForeignKey('status.sh_id'), primary_key=True)