from django.shortcuts import render
from rest_framework import generics,views,status
from rest_framework.response import Response
from .models import Chat
from user.models import UserToken
from middleware.models import Transaction
from .serializers import ChatSerializer
# Create your views here.


class Massages(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    def get_queryset(self):
        return Chat.objects.all()