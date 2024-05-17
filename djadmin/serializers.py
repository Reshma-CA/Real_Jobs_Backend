from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from Listing.models import Job
from users.models import Profile
from rest_framework import serializers

class AdminLoginserializer(ModelSerializer):
    class Meta:
        model= User
        fields = "__all__"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_staff=True)  # Assuming 'is_staff' denotes admins


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"