from django.urls import path
from connect import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
]
