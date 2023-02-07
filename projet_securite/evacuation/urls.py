from django.urls import path, include
from evacuation import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name="index"),

]
urlpatterns += staticfiles_urlpatterns()