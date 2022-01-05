from django.db import models


import uuid


# Create your models here.


class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - id: {self.id}"

    class Meta:
        db_table = "post"
