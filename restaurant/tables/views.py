from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateTableForm
from .models import Table


class TableView(ListView):
    model = Table
    template_name = "tables/tables.html"
    context_object_name = "tables"
    extra_context = {"title": "Столы"}

    def get_queryset(self):
        return Table.objects.all()


class TableCreate(CreateView):
    form_class = CreateTableForm
    model = Table
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("tables")
    extra_context = {
        "title": "Создать стол",
        "button_text": "Создать",
    }


class TableUpdate(UpdateView):
    form_class = CreateTableForm
    model = Table
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("tables")
    pk_url_kwarg = "table_id"
    extra_context = {
        "title": "Изменить стол",
        "button_text": "Изменить",
    }


class TableDelete(DeleteView):
    model = Table
    template_name = "actions/delete.html"
    success_url = reverse_lazy("tables")
    pk_url_kwarg = "table_id"
    extra_context = {"title": "Удаление стола"}
