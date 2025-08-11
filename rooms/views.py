from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.authtoken.models import Token
from . import serializers
from . import models


class RoomTypeListView(ListAPIView):
    queryset = models.RoomType.objects.all() 
    serializer_class = serializers.RoomTypeSerializer
    
class RoomTypeDetailView(RetrieveAPIView):
    queryset = models.RoomType.objects.all()
    serializer_class = serializers.RoomTypeSerializer
    lookup_field='uuid'

class BookingCreateView(CreateAPIView):
    queryset = models.Booking.objects.all() 
    serializer_class = serializers.BookingSerializer

    def post(self,request, *args, **kwargs):
        userToken = request.data['user']
        userObj = Token.objects.get(key=userToken)
        request.data['user'] = userObj.user.id
        return super().post(request, *args, **kwargs)

class RoomsListView(ListAPIView):
    queryset = models.Room.objects.all() 
    serializer_class = serializers.RoomsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(room_type__uuid=self.kwargs['uuid'])
        return qs

class RecentBooking(ListAPIView):
    queryset = models.Booking.objects.all() 
    serializer_class = serializers.BookingSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user__id=self.kwargs['user_id']).order_by('-id')[:1]
        return qs

class MyBooking(ListAPIView):
    queryset = models.Booking.objects.all() 
    serializer_class = serializers.BookingSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user__id=self.kwargs['user_id']).order_by('-id')
        return qs