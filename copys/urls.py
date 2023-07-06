from django.urls import path
from . import views

urlpatterns = [
    path("books/<int:pk>/copys/", views.CopyViews.as_view()),
]
