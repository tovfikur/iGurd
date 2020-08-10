from cryptography.fernet import Fernet
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .login import check_token
# Create your views here.

from .models import UserDetails, UserToken
from wallet.models import WalletDetails
from .serializers import UserSerializer, UserUpdateSerialiser, LoginSerializer, UserRetriveSerializer


def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)


def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)


class UserCreateView(generics.CreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        temp_user_obj = UserDetails.objects.filter(Phone=serializer.data['Phone'])
        temp_wallet_obj = WalletDetails.objects.create(userId=temp_user_obj[0],Cash=0,TotalTransfer=0,TotalWithdraw=0)
        temp_wallet_obj.save()
        return Response({"Created":"Success"}, status=status.HTTP_201_CREATED, headers=headers)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'Phone'

    def get(self, request, *args, **kwargs):
        print(request.META)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        try:
            token = request.data.get('token')
            condition, object = check_token(token)
            print(type(object))
            if type(object) is str:
                return Response({'login': 'Unsuccessful'})
            if not (object.id == self.get_object().id):
                return Response({'login': 'Unsuccessful'})
        except Exception as e:
            return Response({'error':str(e)})
        return self.update(request, *args, **kwargs)


class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user_token_obj = UserToken.objects.filter(token=request.META['CSRF_COOKIE'])
            user_token_obj.delete()
            return Response({'info':'Post like POST object','POST': {'phone':'+8801xxxxxxxxx','password':'xxxxxxxxxxxxx'},'csrf':request.META['CSRF_COOKIE'],'InovID':request.META['INVOCATION_ID']})
        except Exception as e:
            return Response({'info':'Post like POST object','POST': {'phone':'+8801xxxxxxxxx','password':'xxxxxxxxxxxxx'}})

    def post(self, request, *args, **kwargs):
        try:
            user_obj = UserDetails.objects.filter(Phone=request.data['phone'], Password=request.data['password'])
            try:
                UserToken.objects.filter(user=user_obj[0]).delete()
            except Exception:
                pass
            if user_obj[0]:
                print(request.META.get('INVOCATION_ID'))
                key = Fernet.generate_key();
                user_token_obj = UserToken.objects.get_or_create(user=user_obj[0],token=encrypt(request.data['phone'].encode(),key))
        except Exception as e:
            return Response({'error':str(e)})

        try:
            if user_token_obj:
                return Response({'login':'Success','token':user_token_obj[0].token})
        except:
            print('not sending token')
        return  Response({'login':"Doesn't responding"})


class UserApi(generics.RetrieveAPIView):
    # queryset = UserDetails.objects.all()
    def get_queryset(self):
        try:
            token = self.request.META['HTTP_TOKEN']
            token_obj = UserToken.objects.filter(token=token).first().user.id
            obj = UserDetails.objects.filter(id=token_obj)
            return obj
        except Exception as e:
            return UserDetails.objects.filter(id=0)
    serializer_class = UserRetriveSerializer
    lookup_field = "Phone"