from django.urls import path, include
from Extincteur import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("correct", views.correct, name="correct"),
    path("correct2", views.correct2, name="correct"),
    path("incorrect", views.incorrect, name="incorrect"),
    path("fume", views.situation_fume, name="fume"),
    path("", views.situation_Extincteur, name="situation"),
]
urlpatterns += staticfiles_urlpatterns()