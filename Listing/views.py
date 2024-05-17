from django.shortcuts import render
from rest_framework.views import APIView
from .utils import get_id_token_with_code1
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from Listing.models import Job
# from .serializers import ListingSerializer
# Register your models here.
from rest_framework_simplejwt.tokens import AccessToken
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
User = get_user_model()


def authenticate_or_create_user(first_name, last_name, email):
    username = f"{first_name.lower()}{last_name.lower()}"  # Generate username
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
    return user

def get_jwt_token(user):
    token = AccessToken.for_user(user)
    return str(token)


class GoogleLogin(APIView):
    def post(self,request):
        if 'code' in request.data.keys():
            code= request.data['code']
            id_token = get_id_token_with_code1(code)
            first_name = id_token.get('given_name', '')
            last_name = id_token.get('family_name', '')
            email = id_token['email']

            user = authenticate_or_create_user(first_name, last_name, email)
            token = get_jwt_token(user)
            return Response({'access_token': token, 'username': user.username, 'email': email,'id':user.id})

        return Response(status=status.HTTP_400_BAD_REQUEST)

