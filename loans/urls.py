from django.urls import path
from . import views

urlpatterns = [
   path("books/loan/", views.LoanView.as_view()),
   path("books/loan/<int:pk>/", views.LoanDetailView.as_view())
]
