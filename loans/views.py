from django.shortcuts import render
from rest_framework import generics
from loans.models import Loan
from rest_framework_simplejwt.authentication import JWTAuthentication
from loans.serializers import LoanSerializer

# Create your views here.

class LoanView(generics.CreateAPIView):

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()


class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = []

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
