from django import forms

from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro  # Utilizamos el modelo 'Libro' que creamos
        fields = ['titulo', 'autor', 'fecha_publicacion', 'numero_paginas']  # Campos que aparecerán en el formulario
        
        # Personalización de las etiquetas de los campos en el formulario
        labels = {
            'titulo': 'Título del Libro',
            'autor': 'Autor del Libro',
            'fecha_publicacion': 'Fecha de Publicación',
            'numero_paginas': 'Número de Páginas',
        }
        
        # Widgets para personalizar la apariencia de los campos
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numero_paginas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
