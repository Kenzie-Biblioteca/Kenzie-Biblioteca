from django.db import models


class Copy(models.Model):
    created_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copys",
    )
