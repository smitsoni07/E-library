from myadmin.models import *

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories_list': categories}

def scategories_processor(request):
    scategories = Subcategory.objects.all()
    return {'scategories_list': scategories}