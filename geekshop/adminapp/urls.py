from django.urls import path
from adminapp.views import IndexTemlateView, UserListView, UserCreateView, UserUpdateView, UserDeleteViewView, admin_categories, admin_categories_create, admin_products, admin_category_update, admin_category_delete, admin_product_create, admin_product_update, admin_product_delete


app_name = "adminapp"
urlpatterns = [
    path("", IndexTemlateView.as_view(), name="index"),
    path("users/", UserListView.as_view(), name="admin_users"),
    path("user_create/", UserCreateView.as_view(), name="admin_user_create"),
    path("user_update/<int:pk>/", UserUpdateView.as_view(), name="admin_user_update"),
    path("user_delete/<int:pk>/", UserDeleteViewView.as_view(), name="admin_user_delete"),

    path("categories/", admin_categories, name="admin_categories"),
    path("categories_create/", admin_categories_create, name="admin_categories_create"),
    path("category_update/<int:id>/", admin_category_update, name="admin_category_update"),
    path("category_delete/<int:id>/", admin_category_delete, name="admin_category_delete"),

    path("products/", admin_products, name="admin_products"),
    path("product_create/", admin_product_create, name="admin_product_create"),
    path("product_update/<int:id>/", admin_product_update, name="admin_product_update"),
    path("product_delete/<int:id>/", admin_product_delete, name="admin_product_delete")
]
