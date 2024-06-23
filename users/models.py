from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random

# Create your models here.

class User(AbstractUser):
    email= models.EmailField(unique=True)

class Profile(models.Model):
    job_provider = models.OneToOneField(User,on_delete=models.CASCADE)
    agency_name= models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    profile_picture = models.ImageField(blank=True,null=True,upload_to='profile_pictures/%Y/%m/%d/')


    def __str__(self):
        return f"Profile of{self.job_provider}"

#
# class OTP(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     otp = models.CharField(max_length=6)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def is_valid(self):
#         return self.created_at >= timezone.now() - timezone.timedelta(minutes=5)
#
#     def save(self, *args, **kwargs):
#         if not self.otp:
#             self.otp = str(random.randint(100000, 999999))
#         super().save(*args, **kwargs)
