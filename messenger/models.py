from django.db import models
from user.models import UserDetails
from middleware.models import Transaction
# Create your models here.


class Chat(models.Model):
    UserID     = models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING,default=1)
    Transaction= models.ForeignKey(Transaction,on_delete=models.DO_NOTHING,default=1)
    Importance = models.SmallIntegerField(default=0)
    Time       = models.DateTimeField(auto_now_add=True)
    Text       = models.TextField(null=True, blank=True)
    Seen       = models.BooleanField(default=False)


class Notice(models.Model):
    UserID      = models.ForeignKey(UserDetails, on_delete=models.DO_NOTHING, default=1)
    Text        = models.TextField(null=True,blank=True)
    Time        = models.DateTimeField(auto_now_add=True)
    Seen        = models.BooleanField(default=False)