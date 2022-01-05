from django.db import models

import uuid

# Create your models here.


class Project(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - id: {self.id}"

    class Meta:
        db_table = "projects"
