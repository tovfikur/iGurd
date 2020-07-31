from rest_framework import serializers
from .models import UserDetails

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserDetails
		fields = [
			'First name',
			'Last name',
			'District',
			'Upzila',
			'Phone',
			'Email',
			'Password'
		]

class UserUpdateSerialiser(serializers.ModelSerializer):
	class Meta:
		model = UserDetails
		fields = [
			'District',
			'Upzila',
			'Email',
			'Password'
		]

class LoginSerializer(serializers.Serializer):
	PhoneNumber = serializers.IntegerField
	Password	= serializers.CharField