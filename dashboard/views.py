from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.shortcuts import redirect
from accounts.models import VendorProfile, CustomerProfile
from products.models import Product

class RoleRedirectView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return redirect('dashboard:owner_dashboard')
        elif hasattr(user, 'vendorprofile'):
            return redirect('dashboard:vendor_dashboard')
        elif hasattr(user, 'deliveryagent'):
            return redirect('dashboard:delivery_dashboard')
        elif hasattr(user, 'customerprofile'):
            return redirect('dashboard:customer_dashboard')
        else:
            return redirect('accounts:login')
from orders.models import Order

class AdminVendorListView(LoginRequiredMixin, ListView):
    model = VendorProfile
    template_name = 'dashboards/admin_vendor_list.html'
    context_object_name = 'vendors'

class AdminCustomerListView(LoginRequiredMixin, ListView):
    model = CustomerProfile
    template_name = 'dashboards/admin_customer_list.html'
    context_object_name = 'customers'

class AdminProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'dashboards/admin_product_list.html'
    context_object_name = 'products'

class AdminOrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'dashboards/admin_order_list.html'
    context_object_name = 'orders'
    # Removed duplicate RoleRedirectView
    # Removed duplicate views and RoleRedirectView

class OwnerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendors'] = VendorProfile.objects.all()
        context['customers'] = CustomerProfile.objects.all()
        context['products'] = Product.objects.all()
        context['orders'] = Order.objects.all()
        return context

class VendorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/vendor_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendor = self.request.user.vendorprofile
        products = Product.objects.filter(vendor=vendor)
        orders = Order.objects.filter(items__product__vendor=vendor).distinct()
        total_revenue = sum(order.total_amount for order in orders)
        context['products'] = products
        context['orders'] = orders
        context['total_revenue'] = total_revenue
        return context


from orders.models import Order

class CustomerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/customer_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(user=self.request.user).order_by('-created_at')
        context['orders'] = orders
        return context


from orders.models import Order

class DeliveryDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/delivery_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Assuming a deliveryagent field on Order, update as needed
        deliveries = Order.objects.filter(delivery_agent=self.request.user)
        context['deliveries'] = deliveries
        return context
