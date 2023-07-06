from django.db import models
from rest_framework import serializers
from .models import Book
# from users.serializer import UsersSerializer


class BookSerializer(serializers.ModelSerializer):
    # user_id = UsersSerializer(read_only=True) caso queira mostrar tudo
    # user_id = serializers.IntegerField(read_only=True) caso for só o id

    class Meta:
        model = Book
        fields = ["id", "name", "author", "description", "pages"]
