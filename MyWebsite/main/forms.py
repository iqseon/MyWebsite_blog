from .models import Shoes
from django.forms import ModelForm, TextInput


class ShoesForm(ModelForm):
    class Meta:
        model = Shoes
        fields = ("title", "shoe")
        widgets = {
            "title": TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите название обуви'
            }),
            "shoe": TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите модель обуви'
            }),
        }