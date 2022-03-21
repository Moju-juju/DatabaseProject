from django.contrib import admin

# Register your models here.
from .models import (Store, StockList, Staff, Managers, StoreEmployees,
                     Customers, BikeCategory, BikeBrands, BikeProducts,
                     CartItems, Orders)

myModels = [Store, StockList, Staff, Managers, StoreEmployees,
            Customers, BikeCategory, BikeBrands, BikeProducts,
            CartItems, Orders
            ]

for m in myModels:
    admin.site.register(m)

