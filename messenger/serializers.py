from rest_framework import serializers
from .models import Chat, Notice


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'id',
            'UserID',
            'Time',
            'Text',
            'Seen',
            'Importance'
        ]


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = [
            'id',
            'UserID',
            'Time',
            'Text',
            'Seen'
        ]