from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q  # New

def homePage(request):
    return render(request, "catalog/index.html")

def get_all_products(request):
    categories = Category.objects.all()

    searchData = request.GET.get('search')
    if searchData:
        products = Product.objects.filter(Q(name__icontains=searchData) | Q(description__icontains=searchData))
    else:
        products = Product.objects.filter(is_active=True)

    return render(request, "catalog/products.html", {
        "products": products,
        "categories": categories
    })

def get_product_detail(request, product_slug=None):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, "catalog/product-detail.html", {
        'product': product
    })

def get_all_products_by_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=[category]
    )
    return render(request, "catalog/category.html", {"category": category, "products": products})
