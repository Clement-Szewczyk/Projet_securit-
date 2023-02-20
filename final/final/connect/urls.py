from django.urls import path
from django.urls import path
from connect import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # url de la page d'inscription
    path('register/', views.register, name='register'),
    # url de la page de connexion (page d'accueil de l'application)
    path('', views.login, name='login'),
]
# On ajoute les urls des fichiers statiques
urlpatterns += staticfiles_urlpatterns()
