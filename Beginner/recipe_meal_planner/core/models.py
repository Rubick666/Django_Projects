from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.CharField(max_length=100, default="Something")
    name = models.CharField(max_length=100, default="Somthing")
    description = models.CharField(max_length=100, default="Something")

    def __str__(self):
        return self.name