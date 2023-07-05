from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "id",
            "copy_id",
            "user_id",
            "blocked_date",
            "end_blocked_date",
        ]
        extra_kwargs = {
            "id": {"ready_only": True},
            "copy_id": {"ready_only": True},
            "user_id": {"ready_only": True},
        }
