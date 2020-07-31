from django.db import models
from user.models import UserDetails
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Cash(models.Model):
    PhoneNumber         = PhoneNumberField(default='+8801796693300')
    Amount              = models.IntegerField(default=0)
    TrxId               = models.CharField(blank=False, max_length=64,unique=True)


class Transection(models.Model):
    SellerWalletId      = models.IntegerField(blank=True,null=True)
    BuyerWalletId       = models.IntegerField(blank=True,null=True)
    FixedCash           = models.IntegerField(default=None,blank=False)
    Time                = models.DateTimeField(auto_now_add=True)
    paid                = models.BooleanField(default=False)