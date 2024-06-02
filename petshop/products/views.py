from django.shortcuts import render, get_object_or_404, redirect
from .models import MainCategory, Product, SubCategory, AnimalType

# Home Page List Of Products
def product_list(request):
    animal_types_with_subcategories = []
    animal_types = AnimalType.objects.all()

    for animal_type in animal_types:
        subcategories_with_products = []
        main_categories = MainCategory.objects.filter(animal_type=animal_type)[:2]  # محدود کردن به 2 main category
        for main_category in main_categories:
            subcategories = SubCategory.objects.filter(main_category=main_category)[:1]  # محدود کردن به 1 sub category
            for subcategory in subcategories:
                products = Product.objects.filter(sub_category=subcategory)[:10]  # محدود کردن تعداد محصولات به 10
                subcategories_with_products.append({
                    'sub_category': subcategory,
                    'products': products
                })
        if subcategories_with_products:
            animal_types_with_subcategories.append({
                'animal_type': animal_type,
                'subcategories_with_products': subcategories_with_products
            })
    
    return render(request, 'products/home_products_list.html', {
        'animal_types_with_subcategories': animal_types_with_subcategories,
    })


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