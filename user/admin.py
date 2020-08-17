from django.contrib import admin
from .models import UserDetails,UserToken, LoogedIn
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(UserToken)
admin.site.register(LoogedIn)
