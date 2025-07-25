from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from .models import Payment
from .forms import PaymentForm

class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/payment_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.order = get_object_or_404(Order, id=self.kwargs['order_id'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.order = self.order
        form.instance.amount = self.order.total_price
        return super().form_valid(form)

    def get_success_url(self):
        return '/orders/'  # or dashboard or order history
