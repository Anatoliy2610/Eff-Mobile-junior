from django.shortcuts import render

from restaurant.orders.models import Order
from restaurant.statuses.models import Status


def revenue_view(request):
    paid_status = Status.objects.get(name="Оплачено")
    revenue = 0
    for item in Order.objects.filter(status=paid_status):
        for price in item.items.all():
            revenue += price.price

    context = {
        "revenue": revenue,
    }
    return render(request, "revenue.html", context)
