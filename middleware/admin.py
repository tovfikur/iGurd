from django.contrib import admin
from .models import Cash,Transaction, FeeOfTransection
# Register your models here.

admin.site.register(Cash)
admin.site.register(Transaction)
admin.site.register(FeeOfTransection)