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
        return self.request.user.is_authenticated and self.request.user.role == self.role_required
    
class ObjectOwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

