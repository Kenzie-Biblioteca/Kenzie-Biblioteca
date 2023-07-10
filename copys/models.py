from django.db import models
from django.utils import timezone
from django.utils import dates


class Copy(models.Model):

    is_available = models.BooleanField(default=True)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copys",
    )
