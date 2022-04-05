from django.urls import path
from . import views #import the views to access the functions for these urls

#All Url patterns relative to products go here

app_name = 'products'

urlpatterns = [
    path('', views.products, name="products"),
    path('product/<str:pk>/', views.product, name="product"),
    path('create-store/', views.createstore, name="create-store"),
    path('update-product/<str:pk>/', views.updateProject, name='update-product'),
    path('delete-product/<str:pk>/', views.deleteProject, name='delete-product'),
]
