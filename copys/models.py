from django.db import models


class Copy(models.Model):
    class Meta:
        ordering = ("id",)

    created_date = models.DateField()
    end_date = models.DateField()

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copys",
    )
