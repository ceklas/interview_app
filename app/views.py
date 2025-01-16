from rest_framework import viewsets
from .models import Customer, EmployeeDetails, Shipment, PaymentDetails, ShipmentDetails, EmployeeManagesShipment, Membership, Status, Route, Location, User
from .serializers import CustomerSerializer, EmployeeDetailsSerializer, ShipmentSerializer, PaymentDetailsSerializer, ShipmentDetailsSerializer, EmployeeManagesShipmentSerializer, MembershipSerializer, StatusSerializer, RouteSerializer, LocationSerializer, UserSerializer

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