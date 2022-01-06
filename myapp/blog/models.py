from django.db import models

from ckeditor.fields import RichTextField
import uuid


# Create your models here.


class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    image = models.ImageField(verbose_name="Imagen", upload_to="blog/")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    # content = models.TextField(verbose_name="Contenido")
    content = RichTextField(verbose_name="Contenido")

    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    modified_date = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificación")

    def __str__(self):
        return f"{self.title} - id: {self.id}"

    class Meta:
        # Nombre en de la tabla
        db_table = "post"
        # Nombre en el admin
        verbose_name = "Publicación"
        # Nombre en el admin
        verbose_name_plural = "Publicaciones"
        # Ordenar por fecha en el admin
        ordering = ['-created_date']
