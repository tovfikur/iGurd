from django.urls import path, include
from . import views

urlpatterns = [
	path('cash/',views.CashInView.as_view()),
	path('link/create/',views.TransectionView.as_view()),
	path('link/add/',views.AddMeView.as_view())
]
