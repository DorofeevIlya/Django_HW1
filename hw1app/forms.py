from datetime import datetime

from django import forms


class SelectGoods(forms.Form):
    select = forms.ChoiceField(choices=[('add', 'Добавить товар'), ('put' , 'Изменить товар'), ('del', 'Удалить товар')])


class GoodsForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField()
    date_of_add = forms.DateField(initial=datetime.today,
widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    image = forms.ImageField()

class GoodsFormdel(forms.Form):
    pk = forms.IntegerField()

class ImageForm(forms.Form):
    image = forms.ImageField()