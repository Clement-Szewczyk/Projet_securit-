from django.urls import path, include
from alarme import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.sound, name="sound"),

]
urlpatterns += staticfiles_urlpatterns()