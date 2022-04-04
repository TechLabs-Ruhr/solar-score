# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField("Name", max_length=50)
    address = models.CharField("Location", max_length=256, default="Auf der Reihe 2, 45884 Gelsenkirchen, Germany")
    pv = models.DecimalField("Max power", decimal_places=3, max_digits=10, default=15.0)
    
    def __str__(self):
        return self.email

# class UserInformation(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     def __str__(self):
#         return self.userinformation