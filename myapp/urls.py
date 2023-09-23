from django.urls import path
from . import views

# Colocando un punto es como decir en la ruta en la que nos encontramos actualmente.

urlpatterns = [path("", views.hello), path("about/", views.about)]
