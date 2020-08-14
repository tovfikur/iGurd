from django.urls import path, include
from . import views

urlpatterns = [
	path('cash/', views.CashInView.as_view()),
	path('link/create/', views.TransectionView.as_view()),
	path('link/add/', views.AddMeView.as_view()),
	path('link/delete/<id>', views.DeletePayment.as_view()),
	path('link/pay/', views.Pay.as_view()),
	path('link/pre/', views.PrePaymentDetails.as_view()),
	path('my/', views.MyPayments.as_view())
]
