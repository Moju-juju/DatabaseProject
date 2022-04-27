from django import forms
from django.core.exceptions import ValidationError
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
        
        
# class OrderForm(Form):
#     bikes = forms.Choicefield(choices=getMyChoices())
#
#     def getMyChoices(self):
#         choices_list = []
#         return choices_list


class CartItemsForm(ModelForm):
    class Meta:
        model = CartItems
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CartItemsForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CartItemsForm, self).clean()

        selected_BikeProdID = cleaned_data['bike_prod_id']
        order = cleaned_data['order_id']
        selected_StockList = StockList.objects.get(store_id=order.store_staff_id.store_id,
                                                   bike_prod_id=selected_BikeProdID)
        quantitySold = cleaned_data['quantity_sold']
        stockListQuantity = selected_StockList.quantity

        if int(quantitySold) > stockListQuantity:
            raise ValidationError("NOT ENOUGH IN STOCK")
        else:
            selected_StockList.quantity = (selected_StockList.quantity - quantitySold)
            selected_StockList.save()

        return cleaned_data