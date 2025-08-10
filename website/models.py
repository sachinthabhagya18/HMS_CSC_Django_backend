
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from multi_tenancy.models import Tenant
from rooms.models import Booking
from event.models import EventBooking
from django.dispatch import receiver

class Review(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(null=True)
    rating = models.IntegerField(default=1)
    room_booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    event_booking = models.ForeignKey(EventBooking, on_delete=models.SET_NULL, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    
    
class Contact(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, null=True) 
    message = models.TextField(null=True)
    add_time = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_imgs/', null=True)
    mobile = models.CharField(max_length=11, null=True, unique=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)

class Career(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True) 
    email = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True)
    updated_cv = models.FileField(upload_to='cv_files/')
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Banners(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='banner_imgs/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'banners' 

class ControlPanel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to='logo_imgs/')