from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics,views,status
from rest_framework.response import Response
from .models import Chat, Notice
from user.models import UserToken
from middleware.models import Transaction
from .serializers import ChatSerializer, NoticeSerializer
# Create your views here.


class Massages(generics.ListCreateAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        print(self.request.META.get('HTTP_TRANSACTION'))
        obj = Chat.objects.filter(Q(Transaction_id=self.request.META.get('HTTP_TRANSACTION')))
        return obj


class NoticeView(generics.ListAPIView):
    serializer_class = NoticeSerializer

    def get_queryset(self):
        obj = Notice.objects.filter(Q(UserID__usertoken__token=self.request.META.get('HTTP_TOKEN')))
        return obj