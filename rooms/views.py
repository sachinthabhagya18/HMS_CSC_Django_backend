from rest_framework.generics import ListAPIView,RetrieveAPIView
from . import serializers
from . import models


class RoomTypeListView(ListAPIView):
    queryset = models.RoomType.objects.all() 
    serializer_class = serializers.RoomTypeSerializer
    
class RoomTypeDetailView(RetrieveAPIView):
    queryset = models.RoomType.objects.all()
    serializer_class = serializers.RoomTypeSerializer
    lookup_field='uuid'
