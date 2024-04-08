from django.urls import path
from . import views

urlpatterns = [
    path('list_hotels', views.Hotels_list, name='hotelList'),
    path('add_hotel', views.Add_Hotel_to_List, name='addHotel'),
]