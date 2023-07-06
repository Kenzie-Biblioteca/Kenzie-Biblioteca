from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    pages = models.CharField(max_length=50)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="books"
    )
