from django.contrib import admin
from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor")
    list_filter = ("autor",)
    search_fields = ("titulo",)
