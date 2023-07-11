from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView


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


class CustomBookDetailView(BookDetailView):
    def perform_update(self, serializer):
        book = self.get_object()
        serializer.save()
        book.notify_followers()
        # criada para fazer o chamado da notify_followers()


class FollowBookView(APIView):
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        request.user.followed_books.add(book)
        return Response({'message': 'Book followed.'})

    def delete(self, request, book_id):
        book = Book.objects.get(id=book_id)
        request.user.followed_books.remove(book)
        return Response({'message': 'Book unfollowed.'})
