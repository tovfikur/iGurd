from django.shortcuts import render
from rest_framework import generics,views
from rest_framework.response import Response
from .models import Chat
from .serializers import MassageSerializer
# Create your views here.

class Massages(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = MassageSerializer