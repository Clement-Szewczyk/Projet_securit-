from django.urls import path, include
from triangle import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.triangle, name="porte"),
]
urlpatterns += staticfiles_urlpatterns()