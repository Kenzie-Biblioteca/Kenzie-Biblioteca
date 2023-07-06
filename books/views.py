from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookView(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"
