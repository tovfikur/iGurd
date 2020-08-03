from django.urls import path, include
from .views import Massages

urlpatterns = [
   path('', Massages.as_view()),
]