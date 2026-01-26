from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_libros, name="lista_libros"),
    path("autores/nuevo/", views.crear_autor, name="crear_autor"),
    path("libros/nuevo/", views.crear_libro, name="crear_libro"),
    path("libros/<int:libro_id>/prestar/", views.prestar_libro, name="prestar_libro"),
    path("devolver/", views.devolver_libro, name="devolver_libro"),
]
