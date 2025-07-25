from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
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


class CustomerOrderListView(LoginRequiredMixin, ListView):
    template_name = 'orders/my_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

def checkout(request):
    # Dummy checkout view for now
    return render(request, 'orders/checkout.html')
