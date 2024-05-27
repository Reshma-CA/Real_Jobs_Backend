from django.contrib import admin

# Register your models here.
from . models import *
# from.forms import JobForm
# class JobAdmin(admin.ModelAdmin):
#     form = JobForm


admin.site.register(Job)
admin.site.register(JobClick)