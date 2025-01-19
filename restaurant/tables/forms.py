from django import forms

from .models import Table


class CreateTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["table_number"]
        widgets = {
            "table_number": forms.TextInput(
                attrs={"placeholder": "Номер стола", "class": "form-control"}
            ),
        }
