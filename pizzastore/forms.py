from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['title', 'slug', 'description', 'category', 'image', 'price', 'stocks']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stocks': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Имя',
            'slug': 'Слаг',
            'description': 'Описание',
            'category': 'Категория',
            'image': 'Картинка',
            'price': 'Стоимость',
            'stocks': 'Количество на складе',
        }
