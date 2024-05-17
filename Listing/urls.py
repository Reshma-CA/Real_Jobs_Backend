from django.urls import path

from rest_framework_simplejwt.views import TokenVerifyView

from .views import GoogleLogin
urlpatterns = [


    path('google/', GoogleLogin.as_view(),name='Google login'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('ViewDetails/<int:id>/', ViewDetails.as_view(), name='view_details'),

]