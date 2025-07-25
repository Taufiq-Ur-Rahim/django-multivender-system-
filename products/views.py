from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, ProductImage, Category
from .forms import ProductForm
from .mixins import RoleRequiredMixin, ObjectOwnerMixin


# Vendor product list
class ProductListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    role_required = 'Vendor'

    def get_queryset(self):
        vendor_profile = getattr(self.request.user, 'vendorprofile', None)
        if vendor_profile:
            return Product.objects.filter(vendor=vendor_profile)
        return Product.objects.none()

# Customer product catalog
class ProductCatalogView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.all()
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        if search:
            queryset = queryset.filter(name__icontains=search)
        if category:
            queryset = queryset.filter(category_id=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')
    role_required = 'Vendor'

    def form_valid(self, form):
        form.instance.vendor = self.request.user.vendorprofile
        response = super().form_valid(form)
        images = self.request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=self.object, image=image)
        return response

class ProductUpdateView(LoginRequiredMixin, RoleRequiredMixin, ObjectOwnerMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')
    allowed_roles = ['Vendor']
    owner_field = 'vendor'

    def form_valid(self, form):
        response = super().form_valid(form)
        images = self.request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=self.object, image=image)
        return response

class ProductDeleteView(LoginRequiredMixin, RoleRequiredMixin, ObjectOwnerMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')

class ProductDetailView(LoginRequiredMixin, RoleRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    allowed_roles = ['Vendor', 'Customer']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context
    allowed_roles = ['Vendor']
    owner_field = 'vendor'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
