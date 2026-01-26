from django.contrib import admin
from .models import Autor, Libro, Prestamo


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor", "stock")
    list_filter = ("autor",)
    search_fields = ("titulo",)


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "solicitante", "fecha_prestamo", "fecha_devolucion")
    list_filter = ("libro",)
    search_fields = ("solicitante",)
