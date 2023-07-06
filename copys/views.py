from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Copy
from rest_framework.pagination import PageNumberPagination
from .serializers import CopySerializer
from books.models import Book
from rest_framework import generics


class CopyViews(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        find_books = get_object_or_404(Book, id=self.kwargs.get("pk"))
        serializer.save(Books=find_books)
