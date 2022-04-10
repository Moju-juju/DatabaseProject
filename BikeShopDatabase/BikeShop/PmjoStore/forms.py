from django.forms import ModelForm
from .models import Store, Customers, Orders, CartItems


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


class CartItemsForm(ModelForm):
    class Meta:
        model = CartItems
        fields = '__all__'