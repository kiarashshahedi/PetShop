from django.contrib import admin
from .models import Category, Product, ProductImage, Tag

# adding image more than one 
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'is_featured', 'created_at', 'updated_at']
    list_filter = ['available', 'category', 'is_featured', 'created_at', 'updated_at']
    search_fields = ['name', 'category__name', 'manufacturer', ]
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']