from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

from users.models import *
# from .serializers import *

from djadmin.serializers import AdminLoginserializer
from rest_framework.serializers import Serializer
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist

from django.contrib.auth import authenticate  # Import for authentication check

from rest_framework import status


# class AdminLoginAPI(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         print(f"EMEILLLLLLLL {email} PASWORDDDDD {password}")
#         try:
#             found = User.objects.get(email=email)
#         except:
#             return Response({"message": 'NotMatched'})
#
#         hashedpassword = found.password
#         matched = check_password(password, hashedpassword)
#
#         if matched == True:
#             obj = User.objects.get(email=email)
#             serialized_object = AdminLoginserializer(obj)
#
#             allcustdatas = User.objects.all()
#
#             refresh = RefreshToken.for_user(obj)
#             return Response(
#                 {"message": 'Matched', "admindata": serialized_object.data, "accesstoken": str(refresh.access_token),
#                  "refreshtoken": str(refresh)})
#         else:
#             return Response({"message": 'NotMatched'})


# class AdminLoginAPI(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         print(f"EMEILLLLLLLL {email} PASWORDDDDD {password}")
#
#         try:
#             found = User.objects.get(email=email)
#             print(found,'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
#         except ObjectDoesNotExist:  # Use ObjectDoesNotExist instead of catching all exceptions
#             return Response({"message": 'NotMatched'})
#
#         hashedpassword = found.password
#         matched = check_password(password, hashedpassword)
#
#         if matched:
#             serialized_object = AdminLoginserializer(found)  # Pass found directly to serializer
#
#             refresh = RefreshToken.for_user(found)
#             return Response(
#                 {"message": 'Matched', "admindata": serialized_object.data, "accesstoken": str(refresh.access_token),
#                  "refreshtoken": str(refresh)})
#         else:
#             return Response({"message": 'NotMatched'})
#

class AdminLoginAPI(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        print(f"EMEILLLLLLLL {email} PASWORDDDDD {password}")

        try:
            user = authenticate(email=email, password=password)  # Use Django's authenticate
            print(user,'kkkkkkkkkkkkk')

            if user is not None and user.is_staff:
                serialized_object = AdminLoginserializer(user)  # Pass user directly
                refresh = RefreshToken.for_user(user)
                return Response(
                    {"message": 'Matched', "admindata": serialized_object.data, "accesstoken": str(refresh.access_token),
                     "refreshtoken": str(refresh)},
                    status=status.HTTP_200_OK
                )
            else:
                return Response({"message": 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:  # Catch generic exceptions for logging or debugging
            print(f"An error occurred: {e}")
            return Response({"message": 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)