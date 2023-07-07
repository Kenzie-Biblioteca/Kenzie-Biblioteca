from django.db import models
import datetime


class Copy(models.Model):
    created_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(
        default=datetime.date.today() + datetime.timedelta(days=4)
    )
    is_available = models.BooleanField(default=True)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copys",
    )
