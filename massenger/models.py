from django.db import models
from middleware.models import Transaction
from user.models import UserDetails
# Create your models here.


class Chat(models.Model):
    Subject     = models.ForeignKey(Transaction,on_delete=models.DO_NOTHING)
    Replays    = models.ForeignKey('self', on_delete=models.DO_NOTHING)
    Text       = models.TextField
    Time       = models.DateTimeField(auto_now_add=True)



