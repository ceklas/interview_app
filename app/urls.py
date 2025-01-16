# app/urls.py
from django.urls import path, include  # include'yi burada ekliyoruz
from rest_framework.routers import DefaultRouter
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

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

# Swagger Schema
schema_view = get_schema_view(
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
    path('api/', include(router.urls)),  # API'ler için URL'ler
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),  # Redoc UI
]