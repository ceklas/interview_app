from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as yasg_get_schema_view
from drf_yasg import openapi

# Router
router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'employee_details', views.EmployeeDetailsViewSet)
router.register(r'shipments', views.ShipmentViewSet)
router.register(r'payment_details', views.PaymentDetailsViewSet)
router.register(r'shipment_details', views.ShipmentDetailsViewSet)
router.register(r'employee_manages_shipment', views.EmployeeManagesShipmentViewSet)
router.register(r'memberships', views.MembershipViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'routes', views.RouteViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'deliveries', views.DeliveryViewSet)  # Delivery URL ekleniyor

# Swagger Schema
schema_view = yasg_get_schema_view(
    openapi.Info(
        title="Interview App API",
        default_version='v1',
        description="API documentation for the Interview App project",
        contact=openapi.Contact(email="contact@interviewapp.local"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('health/', views.health_check, name='health-check'),
    path('api/', include(router.urls)),  # API'ler için URL'ler
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
    # Diğer SQL sorguları için endpointler
    path('api/customers/count-by-type/', views.customer_count_by_type, name='customer-count-by-type'),
    path('api/customers/count-by-payment-status/', views.customer_count_by_payment_status, name='customer-count-by-payment-status'),
    path('api/customers/count-by-payment-mode/', views.customer_count_by_payment_mode, name='customer-count-by-payment-mode'),
    path('api/shipments/count-by-domain/', views.shipment_count_by_domain, name='shipment-count-by-domain'),
    path('api/customers/membership-duration/', views.customer_by_membership_duration, name='customer-membership-duration'),
]