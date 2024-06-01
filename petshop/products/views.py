from django.shortcuts import render, get_object_or_404, redirect
from .models import MainCategory, Product, SubCategory, AnimalType

# Home Page List Of Products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/home_products_list.html', {'products': products})

# Products Detail pages 
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

# navbar view
def navbar(request):
    animal_types = AnimalType.objects.prefetch_related('main_categories__sub_categories').all()
    return render(request, 'products/.html', {'animal_types': animal_types})

# main Category page
def main_category_view(request, main_category_id):
    main_category = get_object_or_404(MainCategory, id=main_category_id)
    products = Product.objects.filter(main_category=main_category)
    return render(request, 'products/main_category.html', {'main_category': main_category, 'products': products})

#sub Category page
def sub_category_view(request, sub_category_id):
    sub_category = get_object_or_404(SubCategory, id=sub_category_id)
    products = Product.objects.filter(sub_category=sub_category)
    return render(request, 'products/sub_category.html', {'sub_category': sub_category, 'products': products})