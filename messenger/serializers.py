from rest_framework import serializers
from .models import Chat, ChadBody


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
        model = ChadBody
        fields = [
            'Chat',
            'Text',
            'Seen'
        ]