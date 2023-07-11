from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "is_available", "book_id"]
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, data):
        return Copy.objects.create(**data)
