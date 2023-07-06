from django.db import models
from django.utils import timezone


class Loan(models.Model):
    class Meta:
        ordering = ["id"]

    blocked_date = models.DateTimeField(auto_now_add=True)
    end_blocked_date = models.DateField(
        default=timezone.now() + timezone.timedelta(hours=96)
    )
    copy = models.ForeignKey(
        "copys.Copy",
        on_delete=models.PROTECT,
        related_name="loans"
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans"
    )
