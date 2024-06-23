from users.models import Profile

from .serializers import ProfileSerializer,UserDetailsView,ProfileAdmin,ProfileCreateSerializer,UserSerializer
from rest_framework import status
from rest_framework import generics

from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # Adjust permissions as necessary
from rest_framework.exceptions import ValidationError
from django.conf import settings
import requests

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'job_provider'

class ProfilUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'job_provider'


# user data view on admin pannel
class UserDetalsViews(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsView


# user get,edit,dalete
class UserListEditAdmin(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')  # Assuming the id is passed in the URL
        obj = User.objects.get(id=id)
        serializer = UserDetailsView(obj)
        return Response(serializer.data)



    def put(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserDetailsView(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        obj = User.objects.get(id=id)
        obj.delete()
        return Response({'message': 'Person deleted'})









    #############################################################################

#pofile data view on admin pannel

class ProfileListAdmin(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileAdmin

# list profile ADD for job providers list
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = []  # Adjust based on your needs

    def list(self, request):
        queryset = self.get_queryset()
        data = [{"id": user.id, "username": user.username} for user in queryset]
        return Response(data)


# profile ADD
class ProfileCreateAdmin(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer

    def create(self, request, *args, **kwargs):
        job_provider_username = request.data.get('job_provider')
        try:
            job_provider = User.objects.get(username=job_provider_username)
        except User.DoesNotExist:
            raise ValidationError({'job_provider': 'User not found.'})

        if Profile.objects.filter(job_provider=job_provider).exists():
            return Response(
                {'detail': 'A profile with this job provider already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a mutable copy of request.data
        mutable_data = request.data.copy()
        mutable_data['job_provider'] = job_provider.pk

        # Pass the mutable data to the serializer
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # EDIT

class ProfileListEditAdmin(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')  # Assuming the id is passed in the URL
        obj = Profile.objects.get(id=id)
        serializer = ProfileAdmin(obj)
        return Response(serializer.data)

    def put(self, request, id):
        user = Profile.objects.get(id=id)
        serializer = ProfileAdmin(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        user = Profile.objects.get(id=id)
        serializer = ProfileAdmin(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        obj = Profile.objects.get(id=id)
        obj.delete()
        return Response({'message': 'Person deleted'}, status=status.HTTP_204_NO_CONTENT)

