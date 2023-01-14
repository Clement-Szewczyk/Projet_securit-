from django.urls import path, include
from Extincteur import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.extincteur, name="extincteur"),
    path("correct", views.correct, name="correct"),
    path("incorrect", views.incorrect, name="incorrect"),
    path('situation', views.situation, name="situation")
]
urlpatterns += staticfiles_urlpatterns()