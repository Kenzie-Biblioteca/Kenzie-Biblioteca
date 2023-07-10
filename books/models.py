from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    pages = models.CharField(max_length=50)

    user = models.ManyToManyField(
        "users.User", related_name="books"
    )
