from rest_framework import serializers
from . import models
from .models import RoomType

class RoomTypeImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomImage
        fields = ['image']

class RoomTypeSerializer(serializers.ModelSerializer):
    room_type_imgs = RoomTypeImagesSerializer(many=True,read_only=True)
    class Meta:
        model = models.RoomType
        fields = ['uuid','title','details','room_type_imgs','per_day_charges']


class BookingSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    class Meta:
        model = models.Booking
        fields = ['room_no','user','total_guest','checkin_date','checkout_date','booking_amount',
                  'booking_details','booking_date','status','formatted_date']
        
    def get_formatted_date(self, obj):
        return obj.booking_date.strftime('%Y-%m-%d  %H:%M:%S')
        

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ['id','room_type','room_no']