# from django import forms
# from .models import Job
# from django.contrib.gis.geos import Point
#
# class JobForm(forms.ModelForm):
#     latitude = forms.FloatField(required=True)
#     longitude = forms.FloatField(required=True)
#
#     class Meta:
#         model = Job
#         fields = ['title', 'description', 'area', 'borough', 'listing_type',
#                   'price', 'location', 'published_at','picture1','picture2','picture3','picture4','picture5']  # Removed 'latitude' and 'longitude'
#
#     def clean(self):
#         cleaned_data = super().clean()
#         latitude = cleaned_data.get('latitude')
#         longitude = cleaned_data.get('longitude')
#
#         if latitude is None or longitude is None:
#             raise forms.ValidationError("Latitude and longitude are required.")
#
#         cleaned_data['location'] = Point(longitude, latitude, srid=4326)
#         return cleaned_data
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         location= self.initial.get('location')
#         if isinstance(location,Point):
#             self.initial['latitude'] = location.tuple[0]
#             self.initial['longitude'] = location.tuple[1]
#
#
#
#
#
#
#
# # from django import forms
# from.models import Job
# # from django.contrib.gis.geos import Point
#
# # class JobForm(forms.ModelForm):
# #     class Meta:
# #         model = Job
# #         fields = ['title','description','area','borough','listing_type','price','location ',' published_at','latitude','longitude']
# #
# #     latitude = forms.FloatField()
# #     longitude = forms.FloatField()
# #
# #     def clean(self):
# #         data = super().clean()
# #         latitude= data.pop('latitude')
# #         longitude = data.pop('longitude')
# #         data['location'] = Point(latitude,longitude,srid=4326)
# #         return data
#
