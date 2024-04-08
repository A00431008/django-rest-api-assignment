from django.shortcuts import render
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
    hotel_name = hotel_request.get('name', None)
    if hotel_name:
        existing_hotel = Hotel.objects.filter(name=hotel_name).first()
        if existing_hotel:
            return Response({'error': f'Hotel with name "{hotel_name}" already exists'}, status=400)
        else:
            serialize_req_data = HotelSerializer(data=hotel_request)
            if serialize_req_data.is_valid():
                serialize_req_data.save()
                return Response({'Message': "Hotel added successfully to the database"})
    return Response({'error': 'Invalid request or missing hotel name'}, status=400)

    
# API to delete a hotel entry by ID and return its ID
@api_view(['DELETE'])
def Delete_Hotel(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return Response({'Deleted Hotel ID': pk})
    except Hotel.DoesNotExist:
        return Response({'Error': 'Hotel not found'}, status=404)