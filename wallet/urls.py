from django.urls import path, include
from . import views
urlpatterns = [
    path('<id>/',views.WalletView.as_view()),
    path('cash/in/',views.CashInView.as_view())
]
