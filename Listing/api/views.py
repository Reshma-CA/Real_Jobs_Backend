from .serializers import ListingSerializer
from Listing.models import Job
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

class ListingList(generics.ListAPIView):
    queryset = Job.objects.all().order_by('published_at')
    serializer_class = ListingSerializer

class ListingCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'job_provider'

class ViewDetails(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')  # Assuming the id is passed in the URL
        obj = Job.objects.get(id=id)
        serializer = ListingSerializer(obj)
        return Response(serializer.data)


