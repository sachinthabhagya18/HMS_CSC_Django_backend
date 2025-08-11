from django.urls import path
from . import views

urlpatterns = [
    path('room-type/', views.RoomTypeListView.as_view()),  # Added trailing slash
    path('room-type/<str:uuid>/', views.RoomTypeDetailView.as_view()),  # Added trailing slash
    path('booking/', views.BookingCreateView.as_view()), 
    path('rooms/<str:uuid>/', views.RoomsListView.as_view()), 
    path('recent-booking/<int:user_id>/', views.RecentBooking.as_view()), 
    path('my-bookings/<int:user_id>/', views.MyBooking.as_view()), 
]