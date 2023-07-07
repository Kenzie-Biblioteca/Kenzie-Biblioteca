from rest_framework import serializers

from .models import Copy


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "created_date", "end_date", "is_available", "book_id"]
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, data):
        return Copy.objects.create(**data)
