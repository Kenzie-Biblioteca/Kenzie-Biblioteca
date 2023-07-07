from django.db import models


class Loan(models.Model):
    class Meta:
        ordering = ["id"]

    blocked_date = models.DateTimeField(auto_now_add=True)

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
