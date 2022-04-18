from  django.urls import path
from mainapp.views import products, all_products

app_name = "mainapp"
urlpatterns = [
  path("", products, name="products"),
  path("category/<int:id_category>/", products, name="category"),
  path("category/", all_products, name="all_category"),
  path("page/<int:page>", products, name="page")
]
