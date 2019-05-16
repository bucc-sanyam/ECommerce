from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Merchant(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)

class Consumer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)