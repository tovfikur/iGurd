from django.shortcuts import render
from rest_framework import generics,views,status
from rest_framework.response import Response
from .models import Chat,ChatBody
from user.models import UserToken
from middleware.models import Transaction
from .serializers import ChatSerializer, ChatBodySerializer
# Create your views here.


class Massages(generics.ListCreateAPIView):
    serializer_class = ChatBodySerializer

    def get_queryset(self):
        user = UserToken.objects.filter(token=self.request.META.get('HTTP_TOKEN')).first().user
        chat = Chat.objects.filter(UserID=user).first()
        chat_body = ChatBody.objects.filter(Chat=chat)
        # chat_body=ChatBody.objects.all()
        # print(self.request.GET['code'])
        return chat_body

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data['Chat'])
        user = UserToken.objects.filter(token=self.request.META.get('HTTP_TOKEN')).first().user
        chat = Chat.objects.filter(UserId=user)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)