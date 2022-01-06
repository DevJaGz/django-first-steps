from django.contrib import admin

# Models
from .models import Project

# Register your models here.
# admin.site.register(Project)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    # Propiedad para mostrar columnas del modelo
    list_display = ('id', 'title', 'description')
    # Habilita el campo como link para ingresar a editar
    list_display_links = ('id',)
   # Habilita el panel de filtrado y define por cuales campos se hará el filtrado
    list_filter = ('title',)
   # Habilita el panel de busqueda y define por cuales campos se puede realizar una búsqueda
    search_fields = ('id', 'title')
   # Deja el campo como editable. No debe estar en list_display_links
    list_editable = ('title',)
