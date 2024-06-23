from rest_framework import serializers
from users.models import Profile
from Listing.models import Job
from Listing.api.serializers import ListingSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    job_provider_listings = serializers.SerializerMethodField()

    def get_job_provider_listings(self,obj):
        query = Job.objects.filter(job_provider=obj.job_provider)
        listing_serialized = ListingSerializer(query,many=True)
        return listing_serialized.data

    class Meta:
        model= Profile
        fields = '__all__'
#  Admin
#user
class UserDetailsView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}  # Exclude password from response

    def update(self, instance, validated_data):
        # Update fields other than password
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        # Check if password is provided and update if so
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance

# profile


class ProfileAdmin(serializers.ModelSerializer):
    job_provider_username = serializers.SerializerMethodField()
    job_provider = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    def get_job_provider_username(self, obj):
        return obj.job_provider.username

    class Meta:
        model = Profile
        fields = '__all__'

# profile ADD

class ProfileCreateSerializer(serializers.ModelSerializer):
    job_provider = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Profile
        fields = ['job_provider', 'agency_name', 'phone_number', 'bio', 'profile_picture']


  # get job provider only
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']  # Include any fields you need


############################################################################

