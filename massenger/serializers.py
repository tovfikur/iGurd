from rest_framework import serializers
from .models import Chat


class MassageSerializer(serializers.ModelSerializer):
    Replays = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Chat
        fields = [
            'id',
            'UserID',
            'Subject',
            'Replays',
            'Text',
            'Importance',
            'Time',
            'Seen'
        ]
