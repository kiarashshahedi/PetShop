from django.urls import path
from . import views

urlpatterns = [
    
    # home page
    path('', views.product_list, name='home-product-list'),
    
    # product detail page
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
    # category lists
    path('categories/', views.category_list, name='category_list'),
    
    # category details
    path('category/<int:id>/', views.category_detail, name='category_detail'),
    
    # add products out of admin pannel 
    path('add/', views.add_product, name='add_product'),  # Add this line

    
    
]
