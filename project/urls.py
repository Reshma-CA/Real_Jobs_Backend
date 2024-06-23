"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Listing.api import views as Listing_api_views
from users.api import views as users_api_views

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Listing/', Listing_api_views.ListingList.as_view()),
    path('api/Listing/create/', Listing_api_views.ListingCreate.as_view()),

    path('api/Listdetails/<int:id>/', Listing_api_views.ViewDetails.as_view()),

    path('api/profiles/', users_api_views.ProfileList.as_view()),
    path('api/profiles/<int:job_provider>/', users_api_views.ProfileDetail.as_view()),
    path('api/profiles/<int:job_provider>/update/', users_api_views.ProfilUpdate.as_view()),

    # Admin

    path('api/userdetails/', users_api_views.UserDetalsViews.as_view()), # user data
    path('api/userAdminedit/<int:id>/', users_api_views.UserListEditAdmin .as_view()), # user data edit,delete

    path('api/ProfileAdmin/', users_api_views.ProfileListAdmin.as_view()), #  profile data
    path('profiles/create/', users_api_views.ProfileCreateAdmin.as_view()), # profile EDD admin
    path('api/ProfileAdminedit/<int:id>/', users_api_views.ProfileListEditAdmin .as_view()), # profile data edit,delete

     # job create
    path('api/job_providers/',  users_api_views.UserListAPIView.as_view(), name='user-list'), # get only job provider details
    path('api/job/create/', Listing_api_views.JobAdminCreate.as_view()), # job Adding
    path('api/jobEdit/<int:id>/', Listing_api_views.JobListEditAdmin.as_view()), # job Edit,delete

    # Job Click

    path('api/track_click/<int:id>/', Listing_api_views.TrackJobClickView.as_view(), name='track_click'),
    path('api/job_clicks_data/', Listing_api_views.JobClickDataView.as_view(), name='job_clicks_data'),

    # Filters
    path('api/job/filters/', Listing_api_views.JobListfilterView.as_view()),




    path('listing/', include('Listing.urls')),
    path('djadmin/', include('djadmin.urls')),

    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add URL pattern for serving static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
