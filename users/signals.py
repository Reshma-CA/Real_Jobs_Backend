# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from .models import Profile
# User = get_user_model()
# from django.db.models.signals import post_save
#
#
# @receiver(post_save,sender=User)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(job_provider=instance)
#
# @receiver(post_save,sender=User)
# def save_user_profile(sender,instance,**kwargs):
#     instance.profile.save()

from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile
from django.db.models.signals import post_save
User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(job_provider=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(job_provider=instance)
