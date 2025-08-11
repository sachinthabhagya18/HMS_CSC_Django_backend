from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banners  # This is correct
        fields = ['id', 'title', 'image']
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile  # This is correct
        fields = ['mobile']
        
        
# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','password','email','profile']
        
        
#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#         password = validated_data.pop('password')
#         user.set_password(password)
#         user.save()
#         profile_data = validated_data.pop('profile')
#         profile = models.Profile.objects.filter(user=user).update(mobile=profile_data['mobile'])
#         return user


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}  # Important for security
        }
        
    def create(self, validated_data):
        # First extract the profile data
        profile_data = validated_data.pop('profile')
        
        # Create the user without the profile data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password']
        )
        
        # Set the password properly
        profile, created = models.Profile.objects.get_or_create(
            user=user,
            defaults={'mobile': profile_data['mobile']}
        )
        
        if not created:
            # Profile already exists, update it
            profile.mobile = profile_data['mobile']
            profile.save()
        
        return user
    
class UserLoginSerializer(serializers.Serializer):
    mobile =  serializers.CharField()
    password = serializers.CharField()