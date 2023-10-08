from django.urls import path

from .views import ProductViewSet, UserView

urlpatterns = [
    path(
        "products/",
        ProductViewSet.as_view(
            {
                "get": "get_all_products",
                "post": "create_product",
            }
        ),
    ),  # this view is for when /products
    path(
        "products/<int:product_id>",
        ProductViewSet.as_view(
            {
                "get": "get_product",
                "put": "update_product",
                "delete": "delete_product",
            }
        ),
    ),  # this view is for when /products/<product_id>
    path("user/", UserView.as_view()),
]
