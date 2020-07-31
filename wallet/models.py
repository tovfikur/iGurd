from django.db import models
from rest_framework.fields import IntegerField

from user.models import UserDetails
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class WalletDetails(models.Model):
    userId              = models.OneToOneField(UserDetails,on_delete=models.DO_NOTHING)
    Cash                = models.IntegerField(default=0)
    TotalTransfer       = models.IntegerField(default=0)
    TotalWithdraw       = models.IntegerField(default=0)
    LastActive          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CashInHistory(models.Model):
    userId              = models.ForeignKey(WalletDetails,on_delete=models.DO_NOTHING,null=True,blank=True)
    PhoneNumber         = PhoneNumberField(default='+8801796693300')
    Amount              = models.IntegerField(default=0)
    TrxId               = models.CharField(blank=False, max_length=64)