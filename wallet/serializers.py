from rest_framework import serializers
from .models import WalletDetails


class WalletSerializer(serializers.ModelSerializer):
	class Meta:
		model = WalletDetails
		fields = [
			'userId',
			'Cash',
			'TotalTransfer',
			'TotalWithdraw',
		]

class CashInSerializer(serializers.Serializer):
	PhoneNumber = serializers.IntegerField
	TrxId		= serializers.CharField