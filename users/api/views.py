from users.models import Profile

from .serializers import ProfileSerializer,UserDetailsView,ProfileAdmin,ProfileCreateSerializer,UserSerializer
from rest_framework import status
from rest_framework import generics

from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView


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

#pofile data view on admin pannel

class ProfileListAdmin(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileAdmin

# profile ADD
class ProfileCreateAdmin(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer


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
        data = request.data
        obj = Profile.objects.get(id=data['id'])
        serializer = ProfileAdmin(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):
        obj = Profile.objects.get(id=id)
        obj.delete()
        return Response({'message': 'Person deleted'})


class JobProviderProfileView(generics.ListAPIView):
    queryset = User.objects.filter(profile__isnull=False)  # Get users with associated profiles
    serializer_class = UserSerializer  # Assuming this serializer exists