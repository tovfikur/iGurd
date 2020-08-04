from django.db import models
from user.models import UserDetails
# Create your models here.


class Chat(models.Model):
    UserID     = models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING,default=1)
    Importance = models.SmallIntegerField(default=0)
    Time       = models.DateTimeField(auto_now_add=True)


class ChatBody(models.Model):
    Chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    Text = models.TextField(null=True,blank=True)
    Seen = models.BooleanField(default=False)
