from django.shortcuts import render
from rest_framework import generics,views
from rest_framework.response import Response
from middleware.models import Cash
from user.models import UserToken
from .models import CashInHistory
from .models import WalletDetails
from .serializers import WalletSerializer, CashInSerializer
# Create your views here.


class WalletView(generics.RetrieveAPIView):
    queryset = WalletDetails.objects.all()
    serializer_class = WalletSerializer
    lookup_field = 'id'


class CashInView(generics.GenericAPIView):
    serializer_class = CashInSerializer

    def get(self, request):
        return Response({'info':'Post like POST object','POST': {'phone':'+8801xxxxxxxxx','trxid':'xxxxxxxxxxxxx','token':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}})

    def post(self, request, *args, **kwargs):
        try:
            try:
                phone = request.data['phone']
                # trxid = request.data['trxid']
                token = request.data['token']
            except Exception as e:
                return Response({'error':str(e)})
            try:
                middleware_cash_obj = Cash.objects.filter(PhoneNumber = phone)[0] #just a trxid filter for more protection
                token_obj = UserToken.objects.filter(token=token)[0].user
                wallet_obj= WalletDetails.objects.filter(userId=token_obj)[0]
                try:
                    wallet_cash_obj = CashInHistory.objects.create(userId=wallet_obj,PhoneNumber=middleware_cash_obj.PhoneNumber,Amount=middleware_cash_obj.Amount,TrxId=middleware_cash_obj.TrxId)
                    wallet_cash_obj.save()
                    middleware_cash_obj.delete()
                    wallet_obj.Cash = wallet_obj.Cash + wallet_cash_obj.Amount
                    wallet_obj.save()
                except Exception as e:
                    return Response({'error':str(e)})
            except Exception as e:
                return Response({'error':str(e)})
            return Response({'temp_resp':'working'})
        except Exception as e:
            return Response({'error':str(e)})
