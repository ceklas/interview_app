from django.db import models

# Location Modeli
class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"

# Route Modeli
class Route(models.Model):
    start_location = models.ForeignKey(Location, related_name='start_routes', on_delete=models.CASCADE)
    end_location = models.ForeignKey(Location, related_name='end_routes', on_delete=models.CASCADE)
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.start_location.city} -> {self.end_location.city}"

# Shipment Modeli
class Shipment(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('delayed', 'Delayed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    estimated_time = models.IntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shipment {self.id} - {self.status}"

# User Modeli (Gönderici, Alıcı, Kurye)
class User(models.Model):
    USER_TYPE_CHOICES = [
        ('sender', 'Sender'),
        ('receiver', 'Receiver'),
        ('courier', 'Courier'),
    ]
    name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.user_type})"
    
    # Delivery Modeli
class Delivery(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('delayed', 'Delayed'),
    ]

    route = models.ForeignKey('Route', on_delete=models.CASCADE, related_name='deliveries')
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sent_deliveries')
    receiver = models.ForeignKey('User', on_delete=models.CASCADE, related_name='received_deliveries')
    courier = models.ForeignKey('User', on_delete=models.CASCADE, related_name='managed_deliveries')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    estimated_time = models.DurationField()

    def __str__(self):
        return f"Delivery {self.id} from {self.sender.name} to {self.receiver.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "route": str(self.route),  # Assuming route has a string representation
            "sender": self.sender.name,
            "receiver": self.receiver.name,
            "courier": self.courier.name,
            "status": self.status,
            "estimated_time": str(self.estimated_time),
        }

# Membership Modeli
class Membership(models.Model):
    m_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()

    # Relationship
    customers = models.ManyToManyField('Customer', related_name='memberships')

    def __str__(self):
        return f"Membership {self.m_id}"

# Customer Modeli
class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    membership_m_id = models.ForeignKey('Membership', on_delete=models.SET_NULL, null=True)
    cust_name = models.CharField(max_length=30)
    cust_email = models.CharField(max_length=50)
    cust_type = models.CharField(max_length=20, choices=[('Wholesale', 'Wholesale'), ('Retail', 'Retail'), ('Internal Goods', 'Internal Goods')])
    cust_addr = models.CharField(max_length=100)
    cust_cont_no = models.BigIntegerField()

    # Relationship
    shipments = models.ManyToManyField(Shipment, related_name='customers')

    def __str__(self):
        return f"Customer {self.cust_name}"

# PaymentDetails Modeli
class PaymentDetails(models.Model):
    payment_id = models.CharField(max_length=40, primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_status = models.CharField(max_length=10, choices=[('PAID', 'PAID'), ('NOT PAID', 'NOT PAID')])
    payment_mode = models.CharField(max_length=20, choices=[('COD', 'COD'), ('CARD PAYMENT', 'CARD PAYMENT')])
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment {self.payment_id}"

# EmployeeDetails Modeli
class EmployeeDetails(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_designation = models.CharField(max_length=40)
    emp_addr = models.CharField(max_length=100)
    emp_branch = models.CharField(max_length=15)
    emp_cont_no = models.BigIntegerField()

    # Relationship
    managed_shipments = models.ManyToManyField('Shipment', related_name='employees_managed')

    def __str__(self):
        return f"Employee {self.emp_name}"

# Status Modeli
class Status(models.Model):
    sh_id = models.AutoField(primary_key=True)
    current_st = models.CharField(max_length=15)
    sent_date = models.DateField()
    delivery_date = models.DateField()

    # Relationship
    managed_shipments = models.ManyToManyField('Shipment', related_name='statuses')

    def __str__(self):
        return f"Status {self.sh_id}"
    
    # ShipmentDetails Modeli
class ShipmentDetails(models.Model):
    sd_content = models.CharField(max_length=40)
    sd_domain = models.CharField(max_length=20, choices=[('International', 'International'), ('Domestic', 'Domestic')])
    sd_type = models.CharField(max_length=20, choices=[('Express', 'Express'), ('Regular', 'Regular')])
    sd_weight = models.CharField(max_length=10)
    sd_charges = models.IntegerField()
    sd_addr = models.CharField(max_length=100)
    ds_addr = models.CharField(max_length=100)
    
    # Relationship
    payments = models.ForeignKey('PaymentDetails', on_delete=models.CASCADE, related_name='shipment_details', null=True)
    managed_shipments = models.ForeignKey('EmployeeManagesShipment', on_delete=models.CASCADE, related_name='shipment_details', null=True)

    def __str__(self):
        return f"ShipmentDetails {self.sd_id}"

# EmployeeManagesShipment Modeli
class EmployeeManagesShipment(models.Model):
    employee = models.ForeignKey('EmployeeDetails', on_delete=models.CASCADE, related_name='shipments_managed')
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, related_name='managed_by_employees')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name='assigned_to_shipments')

    def __str__(self):
        return f"EmployeeManagesShipment {self.employee} - {self.shipment}"