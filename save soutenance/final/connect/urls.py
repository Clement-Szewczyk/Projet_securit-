from django.urls import path
from django.urls import path
from connect import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
]
urlpatterns += staticfiles_urlpatterns()
