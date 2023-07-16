
from django.shortcuts import render

from medical_shop.models import Product


def home(request):
    all_products = Product.objects.all()
    context = {
        "all_products": all_products
    }
    return render(request, "medical_shop/index.html", context=context)


def products_by_category(request, pk):
    category_products = Product.objects.filter(category_id=pk)
    context = {
        "category_products": category_products
    }
    return render(request, "medical_shop/category.html", context=context)
