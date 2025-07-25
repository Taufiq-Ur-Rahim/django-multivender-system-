from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm
from .mixins import RoleRequiredMixin, ObjectOwnerMixin

# Vendor can only manage their own products
class ProductListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    allowed_roles = ['Vendor']

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user)

class ProductCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')
    allowed_roles = ['Vendor']

    def form_valid(self, form):
        form.instance.vendor = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, RoleRequiredMixin, ObjectOwnerMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')
    allowed_roles = ['Vendor']
    owner_field = 'vendor'

class ProductDeleteView(LoginRequiredMixin, RoleRequiredMixin, ObjectOwnerMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    allowed_roles = ['Vendor']
    owner_field = 'vendor'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
