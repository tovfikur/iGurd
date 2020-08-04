from django.shortcuts import render
from rest_framework import generics,views
from rest_framework.response import Response
from .models import Chat,ChatBody
from user.models import UserToken
from .serializers import ChatSerializer, ChatBodySerializer
# Create your views here.


class Massages(generics.ListCreateAPIView):
    serializer_class = ChatBodySerializer

    def get_queryset(self):
        print(self.request.META)

        return ChatBody.objects.all()