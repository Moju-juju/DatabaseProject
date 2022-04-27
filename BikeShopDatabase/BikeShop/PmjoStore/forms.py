from django import forms
from django.forms import ModelForm, Form, ChoiceField
from .models import BikeBrands, BikeProducts, StockList, Store, Customers, Orders, CartItems


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'


# class OrderForm(Form):
#     bikes = forms.Choicefield(choices=getMyChoices())
#
#     def getMyChoices(self):
#         choices_list = []
#         return choices_list


class CartItemsForm(ModelForm):
    class Meta:
        model = CartItems
        fields = ('bike_prod_id', 'quantity_sold',)


class BrandForm(ModelForm):
    class Meta:
        model = BikeBrands
        fields = '__all__'

    
class ProductsForm(ModelForm):
    class Meta:
        model = BikeProducts
        fields = '__all__'

class StocksForm(ModelForm):
    class Meta:
        model = StockList
        fields = '__all__'
