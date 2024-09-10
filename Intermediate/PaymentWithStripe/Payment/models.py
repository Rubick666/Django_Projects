from django.db import models
from django.utils import timezone

class Subscription(models.Model):
    subscription_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100, null=True)
    customer_email = models.EmailField(null=True)
    amount_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    currency = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    payment_status = models.CharField(max_length=50, null=True)