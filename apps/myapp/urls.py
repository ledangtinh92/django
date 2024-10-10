from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('category/', views.category_list, name='category_list'),
    path('category/add/', views.add_category, name='add_category'),
    path('login/', views.login_view, name='login'),
]