from django.contrib import admin
from .models import PartnerList, PaymentPartner, Testimonials, Index, AboutUsList
# Register your models here.
admin.site.register(Index)
admin.site.register(PartnerList)
admin.site.register(PaymentPartner)
admin.site.register(Testimonials)
admin.site.register(AboutUsList)
