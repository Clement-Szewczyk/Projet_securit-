from django.urls import path, include
from PDR import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.pdr, name="pdr"),
]
urlpatterns += staticfiles_urlpatterns()