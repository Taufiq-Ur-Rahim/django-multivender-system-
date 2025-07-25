from django.urls import path
from .views import VendorOrderListView, AdminOrderListView, CustomerOrderListView
from . import views

app_name = 'orders'

urlpatterns = [
    path('vendor/', VendorOrderListView.as_view(), name='vendor_orders'),
    path('admin/', AdminOrderListView.as_view(), name='admin_orders'),
    # path('update/<int:pk>/', OrderStatusUpdateView.as_view(), name='update_order_status'),
    path('my/', CustomerOrderListView.as_view(), name='my_orders'),
    path('checkout/', views.checkout, name='checkout'),
]
