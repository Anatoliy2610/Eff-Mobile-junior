from django.contrib import admin
from django.urls import include, path

from restaurant import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dishes/", include("restaurant.dishes.urls")),
    path("statuses/", include("restaurant.statuses.urls")),
    path("", include("restaurant.orders.urls")),
    path("tables/", include("restaurant.tables.urls")),
    path("revenue/", views.revenue_view, name="revenue"),
]
