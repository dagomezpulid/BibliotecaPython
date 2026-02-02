from django import forms
from .models import Autor, Libro, Prestamo, MovimientoStock
from django.core.exceptions import ValidationError
from django.utils import timezone


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre del autor"
            })
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "stock"]
        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título del libro"
            }),
            "autor": forms.Select(attrs={
                "class": "form-select"
            }),
            "stock": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0
            }),
        }

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ["solicitante", "fecha_prestamo"]
        widgets = {
            "solicitante": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_prestamo": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
        }


class DevolucionForm(forms.Form):
    solicitante = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    fecha_devolucion = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
        })
    )
    
class AjusteStockForm(forms.Form):
        
    TIPO_CHOICES = (
        ("ENTRADA", "Entrada"),
        ("SALIDA", "Salida"),
    )

    libro = forms.ModelChoiceField(
        queryset=Libro.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"})
    )

    tipo = forms.ChoiceField(
        choices=TIPO_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    motivo = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
