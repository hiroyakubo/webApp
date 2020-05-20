from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("delete_all", views.delete_all, name="delete_all"), 
    path("delete/<int:delete_id>", views.delete_part, name="delete_part"), 
]