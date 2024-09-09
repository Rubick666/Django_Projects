# payments/models.py

from django.db import models

class Subscription(models.Model):
    subscription_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
