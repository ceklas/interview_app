from django.contrib import admin
from .models import *
admin.site.register(Membership)
admin.site.register(EmployeeDetails)
admin.site.register(Status)
admin.site.register(ShipmentDetails)
admin.site.register(Customer)
admin.site.register(PaymentDetails)
admin.site.register(EmployeeManagesShipment)
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(User)
#admin.site.register(Delivery)