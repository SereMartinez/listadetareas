from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index" ),
    path("",views.insert, name="insert"),
    path("delete/<int:task_id>", views.delete, name="delete")

]