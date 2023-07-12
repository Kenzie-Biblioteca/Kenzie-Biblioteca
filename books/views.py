from django.shortcuts import render
from .models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
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
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        request.user.followed_books.add(book)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        request.user.followed_books.add(book)
        return Response(book)


class UnfollowBookView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=self.kwargs.get("pk"))

        request.user.followed_books.remove(book)
        return Response({'message': 'Book unfollowed.'})
