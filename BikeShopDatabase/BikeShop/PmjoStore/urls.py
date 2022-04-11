from django.urls import path
from . import views #import the views to access the functions for these urls

#All Url patterns relative to products go here

app_name = 'PmjoStore'

urlpatterns = [
    path('', views.products, name="products"),
    path('product/<str:pk>/', views.product, name="product"),
    path('create-store/', views.createstore, name="create-store"),
    path('update-product/<str:pk>/', views.updateProject, name='update-product'),
    path('delete-product/<str:pk>/', views.deleteProject, name='delete-product'),
    path('customers/', views.customers, name="customers-page"),
    path('add-customers/', views.createCustomer, name="add-customers"),
    path('update-customer/<str:pk>/', views.updateCustomer, name="update-customer"),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name="delete-customer"),
    path('orders/', views.orders, name="orders-page"),
    path('add-order/', views.createOrder, name="add-order"),
    path('update-order/<str:pk>/', views.updateOrder, name="update-order"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="delete-order"),
    path('lookup/', views.searchPage, name="lookup-page"),
]