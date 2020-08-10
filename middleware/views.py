from django.shortcuts import render
import json
from django.core import serializers
from rest_framework import generics, views, status
from rest_framework.response import Response
from user.login import check_token
from django.db.models import Q
# Create your views here.

from .models import Cash,Transaction
from wallet.models import WalletDetails
from .serializers import CashInSerializer, TransectionSerializer
from user.models import UserDetails,UserToken


class CashInView(generics.CreateAPIView):
    queryset = Cash.objects.all()
    serializer_class = CashInSerializer


class TransectionView(generics.CreateAPIView):
    queryset = Transaction
    serializer_class = TransectionSerializer

    def create(self, request, *args, **kwargs):
        try:
            condition, obj = check_token(request.data['token'])
            wallet         = WalletDetails.objects.all()

            try:
                wallet_user = wallet.get(userId=obj)
                if request.data.get('BuyerWalletId'):
                    buyer_wallet = wallet.get(id=request.data.get('BuyerWalletId'))
                    if not wallet_user == buyer_wallet:
                        return Response({'Wallet':'You are not authorized to use this wallet'})
                    buyer_wallet_obj = wallet.get(userId=obj)
                    if buyer_wallet_obj.Cash >= int(request.data.get('FixedCash')):
                        buyer_wallet_obj.Cash = buyer_wallet_obj.Cash - int(request.data.get('FixedCash'))
                        buyer_wallet_obj.TotalTransfer = buyer_wallet_obj.TotalTransfer + int(request.data.get('FixedCash'))
                        buyer_wallet_obj.save()
                    else:
                        return Response({'Cash': 'Wallet out of money'})
                    if not request.data.get('BuyerWalletId') == request.data.get('Creator'):
                        return Response({"Wallet":"It isn't valid wallet id"})

                elif request.data.get('SellerWalletId'):
                    seller_wallet = wallet.get(id=int(request.data.get('SellerWalletId')))
                    if not wallet_user == seller_wallet:
                        return Response({'Wallet': 'You are not authorized to use this wallet'})
                    if not request.data.get('BuyerWalletId') == request.data.get('Creator'):
                        return Response({"Wallet":"It isn't valid wallet id"})
            except Exception as e:
                print('m1',e)
                return Response({'error':str(e)})
            if type(obj) == str:
                return Response({'login': 'Unsuccessful'})
        except Exception as e:
            return Response({'error':str(e)})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AddMeView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            print(request.GET['code'])
        except Exception:
            return Response({'Example':{'url':'[IP]:[PORT]/middleware/link/add/?code=[INTEGER]','POST':{'code':'[INTEGER]','token':'xxxxxxxxxxxx'}}})
        try:
            tran_obj = Transaction.objects.filter(id = request.GET['code'])[0]
            serialized_obj = serializers.serialize('json', [tran_obj, ])
            serialized_obj = json.loads(serialized_obj)
            print(serialized_obj)
            return Response(serialized_obj)
        except Exception as e:
            print('m2',e)
            return Response({'Info':'Try with correct code'})

    def post(self, request, *args, **kwargs):
        condition, obj = check_token(request.data['token'])
        if type(obj) == str:
            return Response({'login': 'Unsuccessful'})
        try:
            tran_obj = Transaction.objects.filter(id = request.data['code'])[0]
        except Exception as e:
            return Response({'error':str(e),'code':'Invalid'})
        try:
            if tran_obj.SellerWalletId and tran_obj.BuyerWalletId:
                return Response({'Code': 'Already used'})
            elif tran_obj.paid:
                return Response({'Code': 'Already paid'})
            if tran_obj.SellerWalletId:
                wallet_obj = WalletDetails.objects.filter(userId=obj)[0]
                if wallet_obj.Cash < tran_obj.FixedCash:
                    return Response({'Cash': 'Wallet out of money'})
                else:
                    wallet_obj.Cash = wallet_obj.Cash - tran_obj.FixedCash
                    wallet_obj.save()
                tran_obj.BuyerWalletId = wallet_obj.id
                tran_obj.save()
            elif tran_obj.BuyerWalletId:
                wallet_obj = WalletDetails.objects.filter(userId=obj)[0]
                tran_obj.SellerWalletId = wallet_obj.userId
                tran_obj.save()
        except Exception as e:
            print(e)
            return Response({'error':str(e)})
        return Response({'Code':'Added'})


class MyPayments(generics.ListAPIView):
    serializer_class = TransectionSerializer

    def get_queryset(self):
        try:
            token = self.request.META['HTTP_TOKEN']
            condition, user_obj = check_token(self.request.data['token'])
            token_obj = user_obj.id
            obj = Transaction.objects.filter(Q(BuyerWalletId=token_obj) | Q(SellerWalletId=token_obj))
            return obj
        except Exception as e:
            return Transaction.objects.filter(id=0)


class Pay(views.APIView):
    def post(self, request, *args, **kwargs):
        try:
            condition, user_obj = check_token(request.data['token'])
            tran_obj    = Transaction.objects.get(id=request.data.get('code'))
            wallet_obj  = WalletDetails.objects.get(userId=user_obj)
            print(type(tran_obj.BuyerWalletId),type(wallet_obj.id))
            print(tran_obj.BuyerWalletId,wallet_obj.id)
            if tran_obj.BuyerWalletId == wallet_obj.id:
                tran_obj.paid = True
                tran_obj.save()
            else:
                return Response({'code':'You are not authorized to pay this'})
        except Exception as e:
            return Response({'error':str(e)})
        return Response({'working':'working'})