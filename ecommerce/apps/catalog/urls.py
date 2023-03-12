from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("products/", views.get_all_products, name="store_home"),
    path("product/detail/<slug:product_slug>/", views.get_product_detail, name="get_product_detail"),
    path("categories/<slug:category_slug>/", views.get_all_products_by_category, name="store_category")
]