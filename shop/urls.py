from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.prod_list, name='all_products'),
    path('<uuid:category_id>/', views.prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_create, name='product_create'),  # Add new product
    path('product/<uuid:product_id>/edit/', views.product_edit, name='product_edit'),  # Edit product
    path('product/<uuid:product_id>/delete/', views.product_delete, name='product_delete'),  # Delete product
]
