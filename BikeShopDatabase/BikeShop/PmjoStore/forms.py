from django.forms import ModelForm
from .models import Store


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'