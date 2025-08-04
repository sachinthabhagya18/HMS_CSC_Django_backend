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
        fields = ['uuid','title','details','room_type_imgs']