from .serializers import ListingSerializer,JobCreateSerializer,JobClickSerializer,JobClickDataSerializer,JobFilterSerializer
from Listing.models import Job,JobClick
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from Listing.filters import JobFilter

class ListingList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = ListingSerializer

class ListingCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'job_provider'

class ViewDetails(APIView):  # 1, Job details
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')  # Assuming the id is passed in the URL
        obj = Job.objects.get(id=id)
        serializer = ListingSerializer(obj)
        return Response(serializer.data)



class JobAdminCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer

    def create(self, request, *args, **kwargs):
        job_provider_username = request.data.get('job_provider')
        print(f"Received job provider username: {job_provider_username}")  # Debugging line

        if not job_provider_username:
            raise ValidationError({'job_provider': 'This field is required.'})

        try:
            job_provider = User.objects.get(username=job_provider_username)
            print(f"Found user: {job_provider}")  # Debugging line
        except User.DoesNotExist:
            print("User not found.")  # Debugging line
            raise ValidationError({'job_provider': 'User not found.'})

        # Create a mutable copy of request.data
        mutable_data = request.data.copy()
        mutable_data['job_provider'] = job_provider.pk

        # Pass the mutable data to the serializer
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# JOB EDIT, DELETE

class JobListEditAdmin(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')  # Assuming the id is passed in the URL
        obj = Job.objects.get(id=id)
        serializer = ListingSerializer(obj)
        return Response(serializer.data)

    def put(self, request, id):
        user = Job.objects.get(id=id)
        serializer = ListingSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        user = Job.objects.get(id=id)
        serializer = ListingSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        obj = Job.objects.get(id=id)
        obj.delete()
        return Response({'message': 'Person deleted'}, status=status.HTTP_204_NO_CONTENT)

# For Job Click
class TrackJobClickView(generics.CreateAPIView):
    queryset = JobClick.objects.all()
    serializer_class = JobClickSerializer

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        job = get_object_or_404(Job, id=id)
        job.clicks += 1
        job.save()
        JobClick.objects.create(job=job)
        return Response({'message': 'Click tracked successfully', 'clicks': job.clicks}, status=status.HTTP_201_CREATED)

# For Job Count Click Data

class JobClickDataView(generics.ListAPIView):
    serializer_class = JobClickDataSerializer

    def get_queryset(self):
        return JobClick.objects.annotate(date=TruncDate('clicked_at')).values('date', 'job__title').annotate(clicks=Count('id')).order_by('date')

# JOb Filter view

class JobListfilterView(APIView):
    def post(self, request, format=None):
        title = request.data.get('title')
        borough = request.data.get('borough')
        price_range = request.data.get('priceRange')  # Retrieve price range filter

        queryset = Job.objects.all()
        if title:
            queryset = queryset.filter(title__icontains=title)
        if borough:
            queryset = queryset.filter(borough__iexact=borough)
        if price_range:
            min_price, max_price = self.parse_price_range(price_range)
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        serializer = JobFilterSerializer(queryset, many=True)
        if queryset.exists():  # Check if queryset has any results
            return Response({'message': 'successful', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No matching results found', 'data': []}, status=status.HTTP_200_OK)

    def parse_price_range(self, price_range):
        if price_range == '0-500':
            return 0, 500
        elif price_range == '500-1000':
            return 500, 1000
        elif price_range == '1000-1500':
            return 1000, 1500
        else:
            return 0, 9999999  # Default range if price range is not specified or invalid