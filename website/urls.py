from django.urls import path
from . import views

urlpatterns = [
    path('banners',views.BannersList.as_view()),
    path('signup',views.UserCreateview.as_view()),
    path('login',views.UserLoginView.as_view()),
]