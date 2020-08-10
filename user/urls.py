from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('<Phone>/update', views.UserUpdateView.as_view()),
    path('<ACT>/', views.UserApi.as_view()),
]
