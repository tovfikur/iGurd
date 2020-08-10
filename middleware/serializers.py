from rest_framework import serializers
from .models import Cash, Transaction
from wallet.models import WalletDetails
from user.models import UserToken

class CashInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cash
        fields = [
            'PhoneNumber',
            'Amount',
            'TrxId'
        ]


class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'Creator',
            'BuyerWalletId',
            'SellerWalletId',
            'FixedCash',
            'Product',
            'Title',
            'ExtraText',
            'Image1',
            'Image2',
            'Image3',
            'Image4',
            'Image5',
		]
    def validate(self, data):
        wallet_obj = WalletDetails.objects.all()
        if data['BuyerWalletId']:
            try:
                wallet_obj = wallet_obj.get(userId=data['BuyerWalletId'])
            except Exception as e:
                print('s1',e)
                raise serializers.ValidationError({"error": "Buyer wallet id isn't valid"})
        elif data['SellerWalletId']:
            try:
                wallet_obj = wallet_obj.get(userId=data['SellerWalletId'])
            except Exception as e:
                print('s2',e)
                raise serializers.ValidationError({"error": "Seller wallet id isn't valid"})
        if not data['SellerWalletId'] and not data['BuyerWalletId']:
            raise serializers.ValidationError({"error": "(Buyer or Seller) Must insert one"})
        if data['SellerWalletId'] and data['BuyerWalletId']:
            raise serializers.ValidationError({"error": "(Buyer or Seller) You have to add only one"})
        if data['SellerWalletId'] == data['BuyerWalletId']:
            raise serializers.ValidationError({"error": "Buyer and Seller can't be same person"})
        return data
