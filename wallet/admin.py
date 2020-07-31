from django.contrib import admin
from .models import CashInHistory,WalletDetails
# Register your models here.
admin.site.register(WalletDetails)
admin.site.register(CashInHistory)