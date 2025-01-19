from django_filters import FilterSet, ModelChoiceFilter

from restaurant.orders.models import Order, Table
from restaurant.statuses.models import Status


class FilterOrders(FilterSet):
    table_number = ModelChoiceFilter(
        queryset=Table.objects.all(), label="Номер столика"
    )
    status = ModelChoiceFilter(
        queryset=Status.objects.all(), label="Статус заказа"
    )

    class Meta:
        model = Order
        fields = ["table_number", "status"]
