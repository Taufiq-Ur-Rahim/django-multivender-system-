from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from .models import Order
from .forms import OrderStatusForm
from products.models import Product

class VendorOrderListView(LoginRequiredMixin, ListView):
    template_name = 'orders/vendor_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(items__product__vendor=self.request.user).distinct()

class AdminOrderListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'orders/admin_orders.html'
    context_object_name = 'orders'
    queryset = Order.objects.all()

    def test_func(self):
        return self.request.user.is_superuser

class OrderStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderStatusForm
    template_name = 'orders/update_status.html'
    success_url = '/orders/vendor/'  # or redirect back to previous

    def get_queryset(self):
        # Vendors can only update their own product orders
        return Order.objects.filter(items__product__vendor=self.request.user).distinct()
