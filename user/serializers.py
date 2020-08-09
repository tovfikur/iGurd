from rest_framework import serializers
from .models import UserDetails

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserDetails
		fields = [
			'FullName',
			'District',
			'Street',
			'City',
			'zip',
			'Phone',
			'Password'
		]

class UserUpdateSerialiser(serializers.ModelSerializer):
	class Meta:
		model = UserDetails
		fields = [
			'District',
			'Upzila',
			# 'Email',
			'Password'
		]

class LoginSerializer(serializers.Serializer):
	PhoneNumber = serializers.IntegerField
	Password	= serializers.CharField