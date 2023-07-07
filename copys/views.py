from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Copy
from rest_framework.pagination import PageNumberPagination
from .serializers import CopySerializer
from books.models import Book
from rest_framework import generics


class CopyViews(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        id = self.request.data["book_id"]
        get_book = get_object_or_404(Book, id=id)
        serializer.save(book=get_book)
