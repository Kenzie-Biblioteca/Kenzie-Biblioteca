from rest_framework import generics
from loans.models import Loan
from rest_framework_simplejwt.authentication import JWTAuthentication
from loans.serializers import LoanSerializer
from users.models import User
from rest_framework.exceptions import ValidationError
from copys.models import Copy
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404


class LoanView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer):
        copy_id = self.request.data.get("copy_id")
        copy = Copy.objects.get(id=copy_id)
        user_id = self.request.data.get("user_id")
        user = User.objects.get(id=user_id)

        if not copy.is_available:
            raise ValidationError("This book is not available.")

        if user.is_block:
            raise ValidationError("This user is currently blocked, wait 72 hours.")

        copy.is_available = False
        self.returned_rule()
        copy.save()

    def returned_rule(self):
        updated_date = timezone.now()
        returned_date = updated_date + timedelta(hours=96)

        if returned_date.weekday() > 4:
            returned_date.weekday = 0


class LoanDetailView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_update(self, serializer):
        loan = Loan.objects.get(id=copy.id)
        copy = get_object_or_404(Copy, pk=self.kwargs["pk"])

        if loan.book_returned:
            raise ValidationError("This book already returned.")

        copy.is_available = True
        loan.book_returned = True

        copy.save()
        loan.save()
