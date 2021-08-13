from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="product-list"),
    path("create/", views.create, name="create-list"),
    path("update/<int:pk>/", views.update, name="update-list"),
    path("delete/<int:pk>/", views.delete, name="delete-list"),
    
    path("example/", views.category_example_form, name = "example-form  ")
]