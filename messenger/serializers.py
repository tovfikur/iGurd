from rest_framework import serializers
from .models import Chat, ChatBody


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'id',
            'UserID',
            'Time',
        ]

class ChatBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBody
        fields = [
            'Chat',
            'Text',
            'Seen'
        ]