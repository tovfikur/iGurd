from django.contrib import admin
from .models import UserDetails,UserToken
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(UserToken)