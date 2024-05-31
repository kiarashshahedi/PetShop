from .models import Category

def categories_processor(request):
    cat_categories = Category.objects.filter(name__icontains='گربه', parent__isnull=True)
    dog_categories = Category.objects.filter(name__icontains='سگ', parent__isnull=True)
    categories = Category.objects.all()

    return {'cat_categories': cat_categories, 'dog_categories': dog_categories, 'categories': categories}