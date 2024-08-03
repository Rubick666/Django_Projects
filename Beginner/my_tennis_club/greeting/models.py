from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  date = models.DateField(null=True)

  def __str__(self):
    return self.firstname
