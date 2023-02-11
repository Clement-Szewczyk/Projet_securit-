from django.urls import path, include
from final import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.final, name="final"),
    path("triche", views.triche, name="triche"),
    path("export", views.export, name="export"),

]
urlpatterns += staticfiles_urlpatterns()
