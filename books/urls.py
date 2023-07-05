from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.BooksView.as_view()),
    # path("books/<int:pk>/users/", users_views.UsersView.as_view()),
]
