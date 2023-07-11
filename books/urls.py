from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view()),
    # path("books/<int:pk>/users/", users_views.UsersView.as_view()),
    path("books/<int:book_id>/follow/", views.FollowBookView.as_view()),
    path("books/<int:book_id>/unfollow/", views.FollowBookView.as_view()),
]
