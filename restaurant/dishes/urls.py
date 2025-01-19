from django.urls import path

from restaurant.dishes import views

urlpatterns = [
    path("", views.DishesHome.as_view(), name="dishes"),
    path("create/", views.DishesCreate.as_view(), name="dishes_create"),
    path(
        "<int:dishes_id>/update/",
        views.DishesUpdate.as_view(),
        name="dishes_update",
    ),
    path(
        "<int:dishes_id>/delete/",
        views.DishesDelete.as_view(),
        name="dishes_delete",
    ),
]
