from django.forms import ModelForm
from .models import Store, Customers


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'