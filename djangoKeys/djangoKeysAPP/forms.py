from django import forms

class createProduct(forms.Form):
    title = forms.CharField(max_length=50,label = "Введите название товара")
    price = forms.IntegerField(max_length=50, label="Введите цену товара")















