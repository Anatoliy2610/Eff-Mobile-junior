from django.urls import path

from restaurant.orders import views

urlpatterns = [
    path("", views.OrdersHome.as_view(), name="orders"),
    path("create/", views.OrdersCreate.as_view(), name="orders_create"),
    path(
        "<int:order_id>/update/",
        views.OrdersUpdate.as_view(),
        name="orders_update",
    ),
    path(
        "<int:order_id>/delete/",
        views.OrdersDelete.as_view(),
        name="orders_delete",
    ),
]
