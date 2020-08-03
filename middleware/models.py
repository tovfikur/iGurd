from django.db import models
from user.models import UserDetails
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Cash(models.Model):
    PhoneNumber         = PhoneNumberField(default='+8801796693300')
    Amount              = models.IntegerField(default=0)
    TrxId               = models.CharField(blank=False, max_length=64,unique=True)


class Transaction(models.Model):
    SellerWalletId      = models.IntegerField(blank=True,null=True)
    BuyerWalletId       = models.IntegerField(blank=True,null=True)
    FixedCash           = models.IntegerField(default=None,blank=False)
    Time                = models.DateTimeField(auto_now_add=True)
    paid                = models.BooleanField(default=False)
    Product             = models.BooleanField(default=True)
    Title               = models.CharField(blank=False,null=False,max_length=50)
    ExtraText           = models.TextField
    Image1              = models.ImageField(blank=False,null=False)
    Image2              = models.ImageField(blank=False,null=False)
    Image3              = models.ImageField(blank=True)
    Image4              = models.ImageField(blank=True)
    Image5              = models.ImageField(blank=True)