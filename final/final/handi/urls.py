from django.urls import path, include
from handi import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.handi, name='home'),
]
urlpatterns += staticfiles_urlpatterns()
