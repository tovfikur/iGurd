from django.db import models
from middleware.models import Transaction
from user.models import UserDetails
# Create your models here.


class Chat(models.Model):
    UserID     = models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING,default=1)
    Subject    = models.ForeignKey(Transaction,on_delete=models.DO_NOTHING,default=1)
    Replays    = models.ForeignKey('self', on_delete=models.DO_NOTHING,default=1)
    Text       = models.TextField()
    Importance = models.SmallIntegerField(default=0)
    Time       = models.DateTimeField(auto_now_add=True)
    Seen       = models.BooleanField(default=False)