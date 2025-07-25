from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin

class VendorRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_vendor:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

class RoleRequiredMixin(UserPassesTestMixin):
    role_required = None

    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return False
        if self.role_required == 'Vendor':
            return getattr(user, 'is_vendor', False)
        if self.role_required == 'Customer':
            return getattr(user, 'is_customer', False)
        return False
    
class ObjectOwnerMixin:
    owner_field = 'user'  # default, can be overridden in views
    def get_queryset(self):
        qs = super().get_queryset()
        owner_value = getattr(self.request.user, 'vendorprofile', self.request.user)
        return qs.filter(**{self.owner_field: owner_value})

