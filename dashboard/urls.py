
from django.urls import path
from .views import (
    RoleRedirectView,
    OwnerDashboardView,
    VendorDashboardView,
    CustomerDashboardView,
    DeliveryDashboardView,
    AdminVendorListView, AdminCustomerListView, AdminProductListView, AdminOrderListView
)

app_name = 'dashboard'

urlpatterns = [
    path('', RoleRedirectView.as_view(), name='dashboard_redirect'),
    path('owner/', OwnerDashboardView.as_view(), name='owner_dashboard'),
    path('vendor/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('customer/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('delivery/', DeliveryDashboardView.as_view(), name='delivery_dashboard'),
    path('admin/vendors/', AdminVendorListView.as_view(), name='admin_vendors'),
    path('admin/customers/', AdminCustomerListView.as_view(), name='admin_customers'),
    path('admin/products/', AdminProductListView.as_view(), name='admin_products'),
    path('admin/orders/', AdminOrderListView.as_view(), name='admin_orders'),
]
