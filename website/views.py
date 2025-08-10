# from rest_framework.authtoken.models import Token
# from rest_framework.generics import ListAPIView,CreateAPIView,APIView
# from . import serializers
# from . import models

# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, CreateAPIView  # Remove APIView from here
from rest_framework.views import APIView  # Add this import for APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from . import serializers
from . import models
from django.contrib.auth.models import User

class BannersList(ListAPIView):
    serializer_class = serializers.BannersSerializer
    queryset = models.Banners.objects.all()  # This is correct as is
    
class UserCreateview(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()  # This is correct as is
    
class UserLoginView(APIView):
     def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {'error': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        mobile = serializer.validated_data['mobile']
        password = serializer.validated_data['password']

        try:
            profile = models.Profile.objects.get(mobile=mobile)
            user = profile.user
            
            if not user.check_password(password):
                return Response(
                    {'error': 'Invalid password'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'mobile': mobile
            })
            
        except models.Profile.DoesNotExist:
            return Response(
                {'error': 'Invalid mobile number'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class MobileValidateView(APIView):
    def post(self, request):
        serializer = serializers.UserMobileSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {'error': 'Invalid data format', 'details': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        mobile = serializer.validated_data['mobile']

        # Validate mobile number format (basic check)
        if not mobile.isdigit() or len(mobile) != 10:
            return Response(
                {'error': 'Please enter a valid 10-digit mobile number'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = models.Profile.objects.get(mobile=mobile)
            # If you want to send OTP here, add that logic
            return Response({
                'success': True,
                'message': 'Mobile number verified',
                'mobile': mobile
            })
            
        except models.Profile.DoesNotExist:
            return Response(
                {'error': 'This mobile number is not registered. Please sign up first.'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': 'Server error: ' + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class OTPValidateView(APIView):
    def post(self, request):
        serializer = serializers.MobileOTPSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {'error': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        otp = serializer.validated_data['otp']
        
        # Replace this with your actual OTP validation logic
        if otp != '1234':  # Example OTP check
            return Response(
                {'error': 'Invalid OTP'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        return Response({'success': 'OTP validated'})
            
class ChangePasswordView(APIView):
    def post(self, request):
        serializer = serializers.ChangePasswordSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {'error': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = models.Profile.objects.get(mobile=serializer.validated_data['mobile'])
            user = profile.user
            user.set_password(serializer.validated_data['password'])
            user.save()
            
            return Response({'success': 'Password changed successfully'})
            
        except models.Profile.DoesNotExist:
            return Response(
                {'error': 'Invalid mobile number'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        