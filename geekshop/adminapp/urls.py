from django.urls import path
from adminapp.views import index, admin_users, admin_user_create, admin_user_update, admin_user_delete, admin_categories, admin_categories_create, admin_products, admin_category_update, admin_category_delete, admin_product_create, admin_product_update, admin_product_delete


app_name = "adminapp"
urlpatterns = [
    path("", index, name="index"),
    path("users/", admin_users, name="admin_users"),
    path("user_create/", admin_user_create, name="admin_user_create"),
    path("user_update/<int:id>/", admin_user_update, name="admin_user_update"),
    path("user_delete/<int:id>/", admin_user_delete, name="admin_user_delete"),

    path("categories/", admin_categories, name="admin_categories"),
    path("categories_create/", admin_categories_create, name="admin_categories_create"),
    path("category_update/<int:id>/", admin_category_update, name="admin_category_update"),
    path("category_delete/<int:id>/", admin_category_delete, name="admin_category_delete"),

    path("products/", admin_products, name="admin_products"),
    path("product_create/", admin_product_create, name="admin_product_create"),
    path("product_update/<int:id>/", admin_product_update, name="admin_product_update"),
    path("product_delete/<int:id>/", admin_product_delete, name="admin_product_delete")
]
