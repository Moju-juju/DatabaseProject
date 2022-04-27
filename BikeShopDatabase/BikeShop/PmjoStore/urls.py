from django.urls import path
from . import views #import the views to access the functions for these urls

#All Url patterns relative to products go here

app_name = 'PmjoStore'

urlpatterns = [
    path('', views.stores, name="stores"),
    path('store/<str:pk>/', views.store, name="store"),
    path('create-store/', views.createstore, name="create-store"),
    path('update-store/<str:pk>/', views.updateStore, name='update-store'),
    path('delete-store/<str:pk>/', views.deleteStore, name='delete-store'),
    path('customers/', views.customers, name="customers-page"),
    path('add-customers/', views.createCustomer, name="add-customers"),
    path('update-customer/<str:pk>/', views.updateCustomer, name="update-customer"),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name="delete-customer"),
    path('customer-purchases/<str:pk>/', views.purchases, name="customer-purchases"),
    path('orders/', views.orders, name="orders-page"),
    path('add-order/', views.CreateOrder, name="add-order"),
    path('update-order/<str:pk>/', views.updateOrder, name="update-order"),
    path('update-order/<str:pk>/add-item/', views.add_item_to_order, name="add_item_to_order"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="delete-order"),
    path('lookup/', views.searchPage, name="lookup-page"),
    path('stock-controls/', views.stockCtrl, name="stock-controls"),
    path('stock-controls/add-brand/', views.addBrand, name="add-brand"),
    path('stock-controls/add-product/', views.addProduct, name="add-product"),
    path('stock-controls/add-stock/', views.addStock, name="add-stock"),
    path('stock-controls/update-stock/<str:pk>/', views.updateStock, name="update-stock"),
    path('store-sales/', views.pieChart, name="store-sales"),
    path('staff-sales/', views.staff, name="staff-sales"),
    #path('orderDetails/<str:pk>/', views.OrderDetails.as_view(), name="order_details"),
]