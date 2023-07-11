from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView


class BookView(generics.ListCreateAPIView):
    authentication_classes = []
    # criar permissão para que apenas o admin possa cadastrar os livros e que todos possam listar os livros (listar qualquer user)
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
    authentication_classes = []  # passar o jwt aqui estilo de outras entregas
    permission_classes = []

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)  # usar get_for_error_404
        request.user.followed_books.add(book)
        return Response({'message': 'Book followed.'})


class UnfollowBookView(APIView):
    authentication_classes = []  # passar o jwt aqui estilo de outras entregas
    permission_classes = []

    def delete(self, request, book_id):
        book = Book.objects.get(id=book_id)  # usar get_for_error_404
        request.user.followed_books.remove(book)
        return Response({'message': 'Book unfollowed.'})

# passar o id do livro e o token do user no beers
