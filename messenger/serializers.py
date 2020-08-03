from rest_framework import serializers
from .models import Chat


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'id',
            'UserID',
            'Text',
            'Time',
            'Seen'
        ]