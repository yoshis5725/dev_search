
from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.all_projects, name="all_projects"),
    path("projects/<str:pk>/", views.single_project, name="single_project"),
]