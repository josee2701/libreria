"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from libreria import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('libros/', views.ListarLibros.as_view(), name='lista_libros'),
    path('libros/<int:pk>/', views.DetalleLibro.as_view(), name='detalle_libro'),
    path('libros/nuevo/', views.CrearLibro.as_view(), name='crear_libro'),
    path('libros/<int:pk>/editar/', views.ActualizarLibros.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.EliminarLibro.as_view(), name='eliminar_libro'),
]
