from django.urls import path
from . import views

urlpatterns = [
    path('room-type/', views.RoomTypeListView.as_view()),  # Added trailing slash
    path('room-type/<str:uuid>/', views.RoomTypeDetailView.as_view()),  # Added trailing slash
]