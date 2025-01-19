from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django_filters.views import FilterView

from .filters import FilterOrders
from .forms import CreateOrderForm, UpdateOrderForm
from .models import Order


class OrdersHome(FilterView, ListView):
    template_name = "orders/orders.html"
    context_object_name = "orders"
    filterset_class = FilterOrders
    model = Order
    allow_empty = False
    extra_context = {
        "title": "Заказы",
        "button_text": "Посмотреть",
    }

    def get_queryset(self):
        return Order.objects.all()


class OrdersCreate(CreateView):
    form_class = CreateOrderForm
    model = Order
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("orders")
    extra_context = {
        "title": "Создать заказ",
        "button_text": "Создать",
    }


class OrdersUpdate(UpdateView):
    form_class = UpdateOrderForm
    model = Order
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("orders")
    pk_url_kwarg = "order_id"
    extra_context = {
        "title": "Обновить заказ",
        "button_text": "Обновить",
    }


class OrdersDelete(DeleteView):
    model = Order
    template_name = "actions/delete.html"
    success_url = reverse_lazy("orders")
    pk_url_kwarg = "order_id"
    extra_context = {"title": "Удалить заказ"}
