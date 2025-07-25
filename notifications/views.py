from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

# from notifications.utils import notify_user

# # After saving an order
# notify_user(order.vendor.user, f"New order #{order.id} received.")
# notify_user(order.user, f"Your order #{order.id} was placed successfully.")