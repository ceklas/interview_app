from rest_framework import viewsets
from .models import Customer, EmployeeDetails, Shipment, PaymentDetails, ShipmentDetails, EmployeeManagesShipment, Membership, Status, Route, Location, User, Delivery
from .serializers import CustomerSerializer, EmployeeDetailsSerializer, ShipmentSerializer, PaymentDetailsSerializer, ShipmentDetailsSerializer, EmployeeManagesShipmentSerializer, MembershipSerializer, StatusSerializer, RouteSerializer, LocationSerializer, UserSerializer, DeliverySerializer
from django.http import JsonResponse
from .utils import execute_sql_query  # SQL sorgusu çalıştırma fonksiyonu import ediliyor

def health_check(request):
    return JsonResponse({"message": "Hello, World!"})

def customer_count_by_type(request):
    query = 'SELECT customer_type, COUNT(*) FROM customer GROUP BY customer_type ORDER BY COUNT(*) DESC;'
    results = execute_sql_query(query)
    return JsonResponse({"data": results})

def customer_count_by_payment_status(request):
    query = 'SELECT payment_status, COUNT(*) FROM customer GROUP BY payment_status ORDER BY COUNT(*) DESC;'
    results = execute_sql_query(query)
    return JsonResponse({"data": results})

def customer_count_by_payment_mode(request):
    query = 'SELECT payment_mode, COUNT(*) FROM customer GROUP BY payment_mode ORDER BY COUNT(*) DESC;'
    results = execute_sql_query(query)
    return JsonResponse({"data": results})

def shipment_count_by_domain(request):
    query = 'SELECT shipment_domain, COUNT(*) FROM shipment GROUP BY shipment_domain ORDER BY COUNT(*) DESC;'
    results = execute_sql_query(query)
    return JsonResponse({"data": results})

def customer_by_membership_duration(request):
    query = 'SELECT C_ID, M_ID, tenure FROM customer WHERE tenure > 10;'
    results = execute_sql_query(query)
    return JsonResponse({"data": results})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class EmployeeDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

class PaymentDetailsViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer

class ShipmentDetailsViewSet(viewsets.ModelViewSet):
    queryset = ShipmentDetails.objects.all()
    serializer_class = ShipmentDetailsSerializer

class EmployeeManagesShipmentViewSet(viewsets.ModelViewSet):
    queryset = EmployeeManagesShipment.objects.all()
    serializer_class = EmployeeManagesShipmentSerializer

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer