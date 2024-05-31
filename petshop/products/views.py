from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Subcategory
from .forms import ProductForm, ProductImageForm


# Home Page List Of Products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/home_products_list.html', {'products': products})

# home navbar load category and subcategories
def home(request):
    dogs_categories = Category.objects.filter(slug='dogs')
    cats_categories = Category.objects.filter(slug='cats')

    dogs_categories_with_subcategories = [(category, category.subcategories.all()) for category in dogs_categories]
    cats_categories_with_subcategories = [(category, category.subcategories.all()) for category in cats_categories]

    context = {
        'dogs_categories_with_subcategories': dogs_categories_with_subcategories,
        'cats_categories_with_subcategories': cats_categories_with_subcategories,
    }
    return render(request, 'products/navbar.html', context)




# Products Detail pages 
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})


# Category list (most used in navbar)
def category_list(request):
    categories = Category.objects.filter(subcategories__isnull=False).distinct()
    return render(request, 'products/category_list.html', {'categories': categories})

# Category Detail (opening specific category and products)
def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategories = category.subcategories.all()
    return render(request, 'category_detail.html', {'category': category, 'subcategories': subcategories})

# Subcategory detail
def subcategory_detail(request, subcategory_slug):
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
    products = Product.objects.filter(subcategory=subcategory)
    return render(request, 'products/subcategory_detail.html', {'subcategory': subcategory, 'products': products})

# add products to website out of admin pannel 
def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            image = image_form.save(commit=False)
            image.product = product
            image.save()
            return redirect('product_list')
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()

    return render(request, 'products/add_product.html', {
        'product_form': product_form,
        'image_form': image_form
    })
    
    
# navbar view
def navbar(request):
    categories = Category.objects.all()
    return {'categories': categories}