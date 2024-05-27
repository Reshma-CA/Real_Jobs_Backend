from random import choices
from django.contrib.gis.db import models
from django.utils import timezone

from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model
# Register your models here.
User = get_user_model()

class Job(models.Model):
    job_provider = models.ForeignKey(User,on_delete= models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    choices_area= (
        ('kerala','kerala'),
    )
    # company = models.CharField(max_length=100)
    area = models.CharField(max_length=20,blank=True,null=True,choices=choices_area)
    borough = models.CharField(max_length=50,blank=True,null=True)
    choices_listing_type= (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Office', 'Office'),
    )
    listing_type = models.CharField(max_length=20,choices=choices_listing_type)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    published_at = models.DateTimeField(default=timezone.now)
    picture1 = models.ImageField(blank=True,null=True,upload_to='pictures/%Y/%m/%d/')
    picture2 = models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    picture3 = models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    picture4 = models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    picture5 = models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    clicks = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class JobClick(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.job.title}'
