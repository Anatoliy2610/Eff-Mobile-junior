from django import forms

from .models import Dishes


class CreateUpdateDishesForm(forms.ModelForm):
    class Meta:
        model = Dishes
        fields = ["name", "price"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Название блюда", "class": "form-control"}
            ),
            "price": forms.TextInput(
                attrs={
                    "placeholder": "Цена блюда в рублях",
                    "class": "form-control",
                }
            ),
        }
