from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('card', 'Credit/Debit Card'),
        ('jazzcash', 'JazzCash'),
        ('easypaisa', 'EasyPaisa'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, default='Pending')  # Pending, Completed, Failed
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.id} - {self.method} - {self.status}"
