from django.urls import path
from . import views

# Create your views here.
app_name = "board"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk_>", views.detail, name="detail"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk_>", views.edit, name="edit"),
    path("delete/<int:pk_>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
]
