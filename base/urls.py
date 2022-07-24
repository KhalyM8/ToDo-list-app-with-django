from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-task/", views.createTask, name = "create-task"),
    path("delete-task/<str:pk>/", views.deleteTask, name = "delete-task"),
    path("workspace/<str:pk>/", views.workspace, name="workspace"),
    path("create-workspace/", views.createWorkpace, name = "create-workspace"),
    path("delete-workspace/<str:pk>/", views.deleteWorkspace, name="delete-workspace"),
]