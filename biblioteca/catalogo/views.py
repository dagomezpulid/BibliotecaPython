from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo
from .forms import AutorForm, LibroForm, PrestamoForm, DevolucionForm
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

def prestar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if libro.stock <= 0:
        messages.error(request, "No hay stock disponible para este libro.")
        return redirect("lista_libros")

    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.libro = libro
            prestamo.save()

            libro.stock -= 1
            libro.save()

            messages.success(request, "Préstamo registrado correctamente.")
            return redirect("lista_libros")
    else:
        form = PrestamoForm()

    return render(request, "catalogo/prestar_libro.html", {
        "form": form,
        "libro": libro
    })

def devolver_libro(request):
    if request.method == "POST":
        form = DevolucionForm(request.POST)
        if form.is_valid():
            solicitante = form.cleaned_data["solicitante"]
            fecha = form.cleaned_data["fecha_devolucion"]

            prestamo = Prestamo.objects.filter(
                solicitante=solicitante,
                fecha_devolucion__isnull=True
            ).first()

            if not prestamo:
                messages.error(request, "No se encontró un préstamo activo.")
                return redirect("lista_libros")

            prestamo.fecha_devolucion = fecha
            prestamo.save()

            prestamo.libro.stock += 1
            prestamo.libro.save()

            messages.success(request, "Libro devuelto correctamente.")
            return redirect("lista_libros")
    else:
        form = DevolucionForm()

    return render(request, "catalogo/devolver_libro.html", {"form": form})

