from django.urls import path
from . import views

urlpatterns = [
    # path('',views.UserCreateView.as_view()),
    path('create/',views.UserCreateView.as_view()),
    path('login/',views.LoginView.as_view()),
    path('<Phone>/update',views.UserUpdateView.as_view())
]
