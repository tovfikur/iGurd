from django.urls import path, include
from .views import Massages, NoticeView

urlpatterns = [
   path('', Massages.as_view()),
   path('notice/', NoticeView.as_view()),

]