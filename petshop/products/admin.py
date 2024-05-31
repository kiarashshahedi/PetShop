from django.contrib import admin
from .models import Category, Product, ProductImage, Tag, Subcategory

# adding image more than one 
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_in_list', 'category', 'price', 'stock', 'available', 'is_featured', 'created_at', 'updated_at']
    list_filter = ['available', 'category', 'is_featured', 'created_at', 'updated_at']
    search_fields = ['name', 'category__name', 'manufacturer', ]
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parent', 'slug']
    search_fields = ['name']
    

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category')
    prepopulated_fields = {'slug': ('name',)}
       
admin.site.register(Subcategory)
