import uuid
from django.db import models
from django.contrib.auth.models import User


class RoomType(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    details = models.JSONField(null=True)
    
    def __str__(self): 
        return self.title

    
class Room(models.Model):
    room_type=models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_no=models.CharField(max_length=100)
    room_desc=models. TextField(null=True)
    def __str(self):
        return f'{self.room_no}-{self.room_type}'

class Booking(models.Model):
    room_no=models. ForeignKey(Room, on_delete=models.CASCADE)
    user=models. ForeignKey(User, on_delete=models. CASCADE)
    booking_date=models.DateTimeField(auto_now_add=True)
    total_guest=models. IntegerField()
    checkin_date=models.DateField()
    checkout_date=models.DateField()
    booking_amount=models.DecimalField(max_digits=10,decimal_places=2)
    booking_details = models.JSONField(null=True)
    def __str(self):
        return f'{self.room_no.room_no}-{self.user}'
    
class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    txt_id=models.TextField()
    total_amt = models.DecimalField(max_digits=10,decimal_places=2)
    response_data = models.TextField()
    payment_date=models.DateField(auto_now_add=True)
    
class Gallery(models.Model):
    image =  models.ImageField(upload_to='g_imges')
    
class RoomImage(models.Model):
    room_type=models.ForeignKey(RoomType, on_delete=models.CASCADE,null=True,related_name='room_type_imgs')
    image =  models.ImageField(upload_to='room_type_imgs/')
    
    def __str__(self):
        return self.room_type.title