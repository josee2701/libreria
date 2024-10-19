from django import forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import LibroForm
from .models import Libro


class CrearLibro(SuccessMessageMixin, CreateView):
    model = Libro  
    form = LibroForm  
    fields = "__all__"  
    success_message = "¡Libro Creado Correctamente!" 
    template_name = "crear.html"

class ListarLibros(ListView):
    model = Libro  
    template_name = "index.html" 

class DetalleLibro(DetailView):
    model = Libro  
    template_name = "detalles.html"

class ActualizarLibros(SuccessMessageMixin, UpdateView):
    model = Libro  
    form = LibroForm  
    fields = "__all__"  
    success_message = "¡Libros Actualizado Correctamente!" 
    template_name = "actualizar.html"
    
    def get_success_url(self):
        return reverse('leer')  

class EliminarLibro(SuccessMessageMixin, DeleteView):
    model = Libro  
    form = LibroForm
    fields = "__all__"
    template_name = "elimina.html"
    
    def get_success_url(self):
        success_message = "¡Libro Eliminado Correctamente!"  
        messages.success(self.request, (success_message))
        return reverse('leer') 

