from django.contrib import admin

# Register your models here.
from .models import (Store, ZipCode, StockList, Staff, StoreEmployees, Customers, BikeCategory,
                     BikeBrands, BikeProducts, CartItems, Orders)

myModels = [Store, ZipCode, StockList, Staff, StoreEmployees, Customers, BikeCategory, BikeBrands,
            BikeProducts, CartItems, Orders
            ]

for m in myModels:
    admin.site.register(m)
