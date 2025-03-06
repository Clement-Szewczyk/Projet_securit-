from django.urls import path, include
from passage import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.alarme, name="passage"),
    path("extincteur", views.extincteur, name="extincteur"),
    path("porte", views.porte, name="porte"),
    path("fume", views.fume, name="fume"),
    path("securite", views.securite, name="securite"),
    path("evac", views.evac, name="evacuation"),
]
urlpatterns += staticfiles_urlpatterns()
