from django.urls import path
from . import views

urlpatterns = [
    path("copys/", views.CopyViews.as_view()),
]
