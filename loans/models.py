from django.db import models
from django.utils import timezone
from datetime import timedelta


class Loan(models.Model):

    copy = models.ForeignKey(
        "copys.Copy",
        on_delete=models.CASCADE,
        related_name="loans"
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans"
    )

    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=timezone.now()+timedelta(hours=96))
    book_returned = models.BooleanField(default=False, null=True)
