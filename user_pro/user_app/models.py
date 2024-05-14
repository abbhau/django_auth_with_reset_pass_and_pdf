from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserOtp(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)

