from django.urls import path, include

from .views import *

urlpatterns = [

    path("Login/", AdminLoginAPI.as_view(), name="adminLogin"),
    # path("Logout/", AdminLogoutView.as_view(), name="adminLogout"),
    # path('Alldetails/', AdminPersonAPI.as_view(), name="PersonAPI"),
    # path('Person/<int:id>/', AdminPersonDetails.as_view(), name="PersonAPI")

]
