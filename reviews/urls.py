
from django.urls import path
from .views import ReviewCreateView

app_name = 'reviews'

urlpatterns = [
    path('product/<int:pk>/review/', ReviewCreateView.as_view(), name='add_review'),
]
