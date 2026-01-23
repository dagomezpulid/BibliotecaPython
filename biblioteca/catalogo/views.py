from django.shortcuts import render, redirect
from .models import Libro, Autor
from django.http import HttpResponse


def lista_libros(request):
    libros = Libro.objects.select_related("autor").all()
    return render(request, "catalogo/lista_libros.html", {"libros": libros})


def crear_autor(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")

        if nombre and nombre.strip():
            Autor.objects.create(nombre=nombre.strip())
            return redirect("lista_libros")

    return render(request, "catalogo/crear_autor.html")


def crear_libro(request):
    autores = Autor.objects.all()

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        autor_id = request.POST.get("autor")

        if titulo and titulo.strip() and autor_id:
            autor = Autor.objects.get(id=autor_id)
            Libro.objects.create(titulo=titulo.strip(), autor=autor)
            return redirect("lista_libros")

    return render(request, "catalogo/crear_libro.html", {"autores": autores})
