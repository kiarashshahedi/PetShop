from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm, ProductImageForm


# Home Page List Of Products
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/home-products-list.html', {'products': products})


# Products Detail pages 
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})


#Category list (most uses in navbar)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


# Category Detail (opening specific category and products)
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.filter(available=True)
    return render(request, 'products/category_detail.html', {'category': category, 'products': products})


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