from django.urls import path
from .views import (
    RoleRedirectView,
    OwnerDashboardView,
    VendorDashboardView,
    CustomerDashboardView,
    DeliveryDashboardView,
)

urlpatterns = [
    path('', RoleRedirectView.as_view(), name='dashboard_redirect'),
    path('owner/', OwnerDashboardView.as_view(), name='owner_dashboard'),
    path('vendor/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('customer/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('delivery/', DeliveryDashboardView.as_view(), name='delivery_dashboard'),
]
