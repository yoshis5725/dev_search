
from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.all_projects, name="all_projects"),
    path("projects/<str:pk>/", views.single_project, name="single_project"),
    path("create-project/", views.create_project, name="create_project"),
    path("update-project/<str:pk>/", views.update_project, name="update_project"),
    path("delete-project/<str:pk>/", views.delete_project, name="delete_project"),
]