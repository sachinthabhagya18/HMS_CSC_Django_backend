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

        if serializer.is_valid():
            error = None
            try:
                profile = models.Profile.objects.get(mobile=serializer.validated_data['mobile'])
                user = profile.user
                if user.check_password(serializer.validated_data['password']):
                    token, created = Token.objects.get_or_create(user=user)
                    _token = token.key
                else:
                    _token = None
                    error = 'Invalid password!!'
            except models.Profile.DoesNotExist:
                _token = None
                error = 'Invalid mobile!!'
            return Response({'token': _token, 'error': error})

