
from django.urls import path
from .views import PaymentCreateView

app_name = 'payment'

urlpatterns = [
    path('pay/<int:order_id>/', PaymentCreateView.as_view(), name='make_payment'),
]
