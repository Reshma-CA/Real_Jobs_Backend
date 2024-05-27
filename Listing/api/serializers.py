from rest_framework import serializers
from Listing.models import Job
from Listing.models import JobClick
from users.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    job_provider_username = serializers.SerializerMethodField()
    published_at_date = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()


    def get_phone_number(self, obj):
        try:
            # Access the related Profile object associated with the job_provider
            profile = obj.job_provider.profile
            # Access the phone_number attribute from the profile
            phone_number = profile.phone_number
            return phone_number
        except Profile.DoesNotExist:
            return None  # Handle the case where there is no profile associated with the job_provider

    def get_published_at_date(self,obj):
        return obj.published_at.date()

    def get_job_provider_username(self,obj):
        return obj.job_provider.username

    def get_country(self,obj):
        return "India"
    class Meta:
        model = Job
        fields = '__all__'

# admin


class JobCreateSerializer(serializers.ModelSerializer):
    job_provider = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Job
        fields = ['job_provider', 'title', 'description', 'area', 'borough', 'listing_type', 'price', 'latitude', 'longitude', 'picture1']


# For Click


class JobClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobClick
        fields = ['job', 'clicked_at']

# For Click fetching Data

# class JobClickDataSerializer(serializers.Serializer):
#     date = serializers.DateField()
#     clicks = serializers.IntegerField()

class JobClickDataSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    job__title = serializers.CharField()
    clicks = serializers.IntegerField()

    class Meta:
        model = JobClick
        fields = ['date', 'job__title', 'clicks']

  # Filters

class JobFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'