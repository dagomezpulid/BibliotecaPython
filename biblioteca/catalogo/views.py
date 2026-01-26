from django.shortcuts import render, redirect
from .models import Libro
from .forms import AutorForm, LibroForm
from django.contrib import messages



def lista_libros(request):
    libros = Libro.objects.select_related("autor").all()
    return render(request, "catalogo/lista_libros.html", {"libros": libros})


def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado correctamente.")
            return redirect("lista_libros")
    else:
        form = AutorForm()

    return render(request, "catalogo/crear_autor.html", {"form": form})




def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado correctamente.")
            return redirect("lista_libros")
    else:
        form = LibroForm()

    return render(request, "catalogo/crear_libro.html", {"form": form})


