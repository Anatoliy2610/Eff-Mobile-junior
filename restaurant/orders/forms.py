from django import forms

from restaurant.dishes.models import Dishes

from .models import Order


class CreateOrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Dishes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Блюда",
    )

    class Meta:
        model = Order
        fields = ["table_number", "items"]


class UpdateOrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=Dishes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Order
        fields = ["table_number", "items", "status"]
