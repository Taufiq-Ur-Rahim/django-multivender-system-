from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from products.models import Product
from .forms import ReviewForm
from .models import Review

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        form.instance.product = product
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')
