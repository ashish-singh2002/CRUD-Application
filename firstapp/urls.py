from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Insert, name="insertpage"),
    path("insert/", views.InsertData, name="insert"),
    path("show/", views.show, name="show"),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("update/<int:pk>", views.update, name="update"),
    path("delete/<int:pk>",views.delete, name="delete"),
]
    