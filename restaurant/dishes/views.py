from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateUpdateDishesForm
from .models import Dishes


class DishesHome(ListView):
    model = Dishes
    template_name = "dishes/dishes.html"
    context_object_name = "dishes"
    extra_context = {"title": "Блюда"}

    def get_queryset(self):
        return Dishes.objects.all()


class DishesCreate(CreateView):
    form_class = CreateUpdateDishesForm
    model = Dishes
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("dishes")
    extra_context = {
        "title": "Создать блюдо",
        "button_text": "Создать",
    }


class DishesUpdate(UpdateView):
    form_class = CreateUpdateDishesForm
    model = Dishes
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("dishes")
    pk_url_kwarg = "dishes_id"
    extra_context = {
        "title": "Изменить блюдо",
        "button_text": "Изменить",
    }


class DishesDelete(DeleteView):
    model = Dishes
    template_name = "actions/delete.html"
    success_url = reverse_lazy("dishes")
    pk_url_kwarg = "dishes_id"
    extra_context = {"title": "Удаление блюдо"}
