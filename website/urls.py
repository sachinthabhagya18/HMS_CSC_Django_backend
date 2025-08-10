from django.urls import path
from . import views

urlpatterns = [
    path('banners',views.BannersList.as_view()),
    path('signup',views.UserCreateview.as_view()),
    path('login',views.UserLoginView.as_view()),
    path('mobile-validate',views.MobileValidateView.as_view()),
    path('otp-validation',views.OTPValidateView.as_view()),
    path('change-password',views.ChangePasswordView.as_view()),
    
]