from django.urls import path

from restaurant.tables import views

urlpatterns = [
    path("", views.TableView.as_view(), name="tables"),
    path("create/", views.TableCreate.as_view(), name="table_create"),
    path(
        "<int:table_id>/update/",
        views.TableUpdate.as_view(),
        name="table_update",
    ),
    path(
        "<int:table_id>/delete/",
        views.TableDelete.as_view(),
        name="table_delete",
    ),
]
