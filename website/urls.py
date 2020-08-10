from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('toc', views.toc),
    path('otp', views.phone_otp),
    path('signup', views.signup),
    path('restore', views.restore_password),
    path('privacy', views.privacy),
    path('join', views.join_as_partner),
    path('inside', views.inside_escrow),
    path('calc', views.cash_calculator),
    path('edit',  views.edit_ac),
    path('dash', views.dashboard),
    path('contact', views.contact)
]
