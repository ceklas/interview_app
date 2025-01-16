from django.db import models

# customer Modeli
class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    membership_m_id = models.ForeignKey('Membership', on_delete=models.SET_NULL, null=True)
    cust_name = models.CharField(max_length=30)
    cust_email = models.CharField(max_length=50)
    cust_type = models.CharField(max_length=20, choices=[('Wholesale', 'Wholesale'), ('Retail', 'Retail'), ('Internal Goods', 'Internal Goods')])
    cust_addr = models.CharField(max_length=100)
    cust_cont_no = models.BigIntegerField()

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"Customer {self.cust_name}"

# employee_details Modeli
class EmployeeDetails(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_designation = models.CharField(max_length=40)
    emp_addr = models.CharField(max_length=100)
    emp_branch = models.CharField(max_length=15)
    emp_cont_no = models.BigIntegerField()

    class Meta:
        db_table = 'employee_details'

    def __str__(self):
        return f"Employee {self.emp_name}"

# employee_manages_shipment Modeli
class EmployeeManagesShipment(models.Model):
    employee = models.ForeignKey('EmployeeDetails', on_delete=models.CASCADE, related_name='shipments_managed')
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, related_name='managed_by_employees')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, related_name='assigned_to_shipments')

    class Meta:
        db_table = 'employee_manages_shipment'

    def __str__(self):
        return f"EmployeeManagesShipment {self.employee} - {self.shipment}"

# membership Modeli
class Membership(models.Model):
    m_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'membership'

    def __str__(self):
        return f"Membership {self.m_id}"

# payment_details Modeli
class PaymentDetails(models.Model):
    payment_id = models.CharField(max_length=40, primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_status = models.CharField(max_length=10, choices=[('PAID', 'PAID'), ('NOT PAID', 'NOT PAID')])
    payment_mode = models.CharField(max_length=20, choices=[('COD', 'COD'), ('CARD PAYMENT', 'CARD PAYMENT')])
    payment_date = models.DateField()

    class Meta:
        db_table = 'payment_details'

    def __str__(self):
        return f"Payment {self.payment_id}"

# shipment_details Modeli
class ShipmentDetails(models.Model):
    sd_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    sd_content = models.CharField(max_length=40)
    sd_domain = models.CharField(max_length=20, choices=[('International', 'International'), ('Domestic', 'Domestic')])
    sd_type = models.CharField(max_length=20, choices=[('Express', 'Express'), ('Regular', 'Regular')])
    sd_weight = models.CharField(max_length=10)
    sd_charges = models.IntegerField()
    sd_addr = models.CharField(max_length=100)
    ds_addr = models.CharField(max_length=100)

    class Meta:
        db_table = 'shipment_details'

    def __str__(self):
        return f"ShipmentDetails {self.sd_id}"

# status Modeli
class Status(models.Model):
    sh_id = models.AutoField(primary_key=True)
    current_st = models.CharField(max_length=15)
    sent_date = models.DateField()
    delivery_date = models.DateField()

    class Meta:
        db_table = 'status'

    def __str__(self):
        return f"Status {self.sh_id}"

# shipment Modeli
class Shipment(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('delayed', 'Delayed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    estimated_time = models.IntegerField(null=True)  # Null yapılabilir
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    sd_content = models.CharField(max_length=255)
    sd_domain = models.CharField(max_length=255)
    sd_type = models.CharField(max_length=255)
    sd_weight = models.CharField(max_length=255)
    sd_charges = models.DecimalField(max_digits=10, decimal_places=2)
    sd_addr = models.CharField(max_length=255)
    ds_addr = models.CharField(max_length=255)

    class Meta:
        db_table = 'shipment'

    def __str__(self):
        return f"Shipment {self.id} - {self.status}"

# route Modeli
class Route(models.Model):
    start_location = models.CharField(max_length=255)  # Location ile ilişki kaldırıldı
    end_location = models.CharField(max_length=255)  # Location ile ilişki kaldırıldı
    distance = models.IntegerField()

    class Meta:
        db_table = 'route'

    def __str__(self):
        return f"{self.start_location} -> {self.end_location}"

# location Modeli
class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'location'

    def __str__(self):
        return f"{self.city}, {self.country}"

# user Modeli
class User(models.Model):
    USER_TYPE_CHOICES = [
        ('sender', 'Sender'),
        ('receiver', 'Receiver'),
        ('courier', 'Courier'),
    ]
    name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.name} ({self.user_type})"