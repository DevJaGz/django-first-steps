from django.contrib import admin

# Models
from .models import Post

# Register your models here.

# Anexar el modelo en el dashboard del admin para editar
# admin.site.register(Post)


# Anexar el modelo en el dashboard del admin para editar, además habilitar nuevas funcionalidades para el dashboard
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Propiedad para mostrar columnas del modelo
    list_display = ('id', 'title', 'image', 'description', 'created_date')
    # Habilita el campo como link para ingresar a editar
    list_display_links = ('id', 'title',)
   # Habilita el panel de filtrado y define por cuales campos se hará el filtrado
    list_filter = ('created_date',)
   # Habilita el panel de busqueda y define por cuales campos se puede realizar una búsqueda
    search_fields = ('id', 'title')

    # ver campos de solo lectura
    readonly_fields = ('created_date', 'modified_date')
