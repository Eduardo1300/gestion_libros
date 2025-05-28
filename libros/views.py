from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    query = request.GET.get('q', '')  # obtener parámetro de búsqueda 'q'
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)  # filtro por título (case-insensitive)
    else:
        libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros, 'query': query})
