from django.db import models
from user.models import UserDetails
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Cash(models.Model):
    PhoneNumber         = PhoneNumberField(default='+8801796693300')
    Amount              = models.IntegerField(default=0)
    TrxId               = models.CharField(blank=False, max_length=64,unique=True)


class Transaction(models.Model):
    Creator             = models.ForeignKey(UserDetails,blank=False,null=False, on_delete=models.DO_NOTHING, related_name='Creator_of_this_transaction',default=1)
    SellerWalletId      = models.ForeignKey(UserDetails,blank=True,null=True, on_delete=models.DO_NOTHING, related_name='Seller_of_this_transection',default=1)
    BuyerWalletId       = models.ForeignKey(UserDetails,blank=True,null=True,on_delete=models.DO_NOTHING,related_name='Buyer_of_this_transection',default=1)
    FixedCash           = models.IntegerField(default=None,blank=False)
    Time                = models.DateTimeField(auto_now_add=True)
    paid                = models.BooleanField(default=False)
    Product             = models.BooleanField(default=True)
    Title               = models.CharField(blank=False,null=False,max_length=50,default='Write a TITLE')
    ExtraText           = models.TextField
    Image1              = models.ImageField(blank=True,null=True)
    Image2              = models.ImageField(blank=True,null=True)
    Image3              = models.ImageField(blank=True,null=True)
    Image4              = models.ImageField(blank=True,null=True)
    Image5              = models.ImageField(blank=True,null=True)