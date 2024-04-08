from django.shortcuts import render
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# API to get hotels' list from database
@api_view(['GET'])
def Hotels_list(request):
    hotels_list = Hotel.objects.all()
    hotelSerializer = HotelSerializer(hotels_list, many=True)
    return Response(hotelSerializer.data)

# API to add hotel to the database
@api_view(['POST'])
def Add_Hotel_to_List(request):
    hotel_request = request.data
    serialize_req_data = HotelSerializer(data=hotel_request)
    if serialize_req_data.is_valid():
        serialize_req_data.save()
        return Response({'Message': "Hotel added successfully to the database"})