from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserDetails(models.Model):
    Fname   	= models.CharField(default=None,max_length=20,name='First name')
    Lname		= models.CharField(default=None,max_length=20,name='Last name')
    District	= models.CharField(default=None,max_length=10)
    Upzila		= models.CharField(default=None,max_length=10)
    Phone		= PhoneNumberField(default='+8801796693300',unique=True)
    # Email       =models.CharField(null=True,max_length=50,blank=True,unique=True)
    ACT			= models.BooleanField(default=True)
    Password	= models.CharField(null=False,default=None,max_length=16)

    def __str__(self):
        return str(self.Phone)


class Notifications(models.Model):
    UserId      = models.ForeignKey(UserDetails,blank=False,null=False, on_delete=models.CASCADE)
    Massage     = models.TextField
    Importance  = models.SmallIntegerField(default=0)
    Seen        = models.BooleanField(default=False)


class UserToken(models.Model):
    user    = models.OneToOneField(UserDetails,on_delete=models.CASCADE,blank=False)
    token   = models.CharField(unique=True,blank=False,default='0',max_length=256)