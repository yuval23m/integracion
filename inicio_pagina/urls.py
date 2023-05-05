
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import index, contacto, productos

urlpatterns = [
    path ('inicio/', index, name="Inicio"),
    path ('productos/', productos, name="productos"),
    path ('contacto/', contacto, name="contacto"),
]