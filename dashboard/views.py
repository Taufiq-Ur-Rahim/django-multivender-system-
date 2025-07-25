from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect

class RoleRedirectView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return redirect('owner_dashboard')
        elif hasattr(user, 'vendor'):
            return redirect('vendor_dashboard')
        elif hasattr(user, 'deliveryagent'):
            return redirect('delivery_dashboard')
        elif hasattr(user, 'customer'):
            return redirect('customer_dashboard')
        else:
            return redirect('login')

class OwnerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/owner_dashboard.html'

class VendorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/vendor_dashboard.html'

class CustomerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/customer_dashboard.html'

class DeliveryDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/delivery_dashboard.html'
