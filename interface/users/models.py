# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pv = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email

# class UserInformation(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     def __str__(self):
#         return self.userinformation