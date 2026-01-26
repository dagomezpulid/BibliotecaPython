from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    solicitante = models.CharField(max_length=100)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.solicitante}"

