from django.shortcuts import render
from rest_framework import generics,views
from rest_framework.response import Response
from .models import Chat,ChatBody
from .serializers import ChatSerializer, ChatBodySerializer
# Create your views here.


class Massages(generics.ListCreateAPIView):
    serializer_class = ChatBodySerializer
    queryset = ChatBody.objects.all()