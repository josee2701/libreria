# Create your models here.
from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    fecha_publicacion = models.DateField(verbose_name="Fecha de Publicación")
    numero_paginas = models.PositiveIntegerField(verbose_name="Número de Páginas")

    def __str__(self):
        return self.titulo  # Esto muestra el título del libro como representación del objeto
