from rest_framework import serializers
from Listing.models import Job
from users.models import Profile

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

# class ListIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Job
#         fields = '__all__'