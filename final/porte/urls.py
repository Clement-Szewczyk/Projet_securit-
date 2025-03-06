from django.urls import path, include
from porte import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.porte, name="porte"),
]
urlpatterns += staticfiles_urlpatterns()