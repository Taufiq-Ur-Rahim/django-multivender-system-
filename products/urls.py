from django.urls import path
from .views import (
    ProductListView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, ProductDetailView, ProductCatalogView
)

app_name = 'products'

urlpatterns = [
    path('', ProductCatalogView.as_view(), name='product_list'),
    path('vendor/', ProductListView.as_view(), name='vendor_product_list'),
    path('add/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
