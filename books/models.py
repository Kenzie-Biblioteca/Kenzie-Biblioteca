from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    pages = models.CharField(max_length=50)

    user = models.ManyToManyField(
        "users.User", on_delete=models.CASCADE, related_name="user_order"
    )
