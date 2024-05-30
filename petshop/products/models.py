from django.db import models

#category of products
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    description = models.TextField(blank = True)
        
    def __str__(self):
        return self.name 
        
        
#product class         
class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,  verbose_name='دسته‌بندی')
    name = models.CharField(max_length=255, verbose_name='نام')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')
    stock = models.PositiveIntegerField(verbose_name='موجودی') 
    available = models.BooleanField(default=True, verbose_name='موجود است/نیست') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی') 
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='وزن بر اساس کیلوگرم')
    dimensions = models.CharField(max_length=100, blank=True, verbose_name='ابعاد به صورت متنی')
    manufacturer = models.CharField(max_length=255, blank=True, verbose_name='اسم سازنده (برند)')
    warranty = models.CharField(max_length=255, blank=True, verbose_name='اطلاعات گارانتی')
    color = models.CharField(max_length=50, blank=True, verbose_name='رنگ محصول')
    breed = models.CharField(max_length=50, blank=True, verbose_name='نژاد') 
    life_stage = models.CharField(max_length=50, blank=True, verbose_name='مرحله زندگی مناسب (سن)')
    flavor = models.CharField(max_length=50, blank=True, verbose_name='طعم دهنده ') 
    nutritional_info = models.TextField(blank=True, verbose_name='اطلاعات تغذیه ای')
    recommended_usage = models.TextField(blank=True, verbose_name='دستورالعمل استفاده توصیه شده') 
    expire_date = models.DateField(null=True, blank=True, verbose_name='تاریخ انقضا')
    origin_country = models.CharField(max_length=100, blank=True, verbose_name='کشور سازنده')  
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='برچسب ها برای جستجو و فیلتر')
    is_featured = models.BooleanField(default=False, verbose_name='تخفیف')
    featured_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='قیمت تخفیف خورده')
    
    
    
# product images 
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='تصویر')

    def __str__(self):
        return f'{self.product.name} Image'
    
    
# tags model 
class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')

    def __str__(self):
        return self.name