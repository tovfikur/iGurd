from rest_framework import serializers
from .models import UserDetails, LoggedIn


class UserRetriveSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserDetails
		fields = [
			'id',
			'FullName',
			'District',
			'Street',
			'City',
			'zip',
			'Phone',
		]

		
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


class LoggedInSerializer(serializers.ModelSerializer):
	class Meta:
		model = LoggedIn
		fields = [
			'device'
		]