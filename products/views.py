from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cart.forms import CartAddProductForm


# Create your views here.
def index(request):
    """Домашняя страница"""
    new_products = Product.objects.order_by('-date_at')[:3]
    return render(request, 'products/index.html', context={'new_products': new_products})


def get_products(request):
    """Страница со всеми продуктами"""
    products = Product.objects.filter(is_active=True)
    paginator = Paginator(products, 6)
    try:
        num = request.GET.get('page', '1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)

    context = {
        'title': 'Shop - Каталог',
        'categories': Category.objects.all(),
        'page': number,
        'paginator': paginator

    }
    return render(request, 'products/products.html', context=context)


def get_category(request, url):
    """Категория и товары этой категории"""
    category = Category.objects.get(slug=url)
    products = category.products.filter(is_active=True),
    paginator = Paginator(products, 6)
    try:
        num = request.GET.get('page', '1')
        number = paginator.page(num)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': Category.objects.all(),
        'page': number,
        'paginator': paginator,
    }
    return render(request, 'products/category.html', context=context)


def detail_product(request, url, pk):
    form = CartAddProductForm()
    product = get_object_or_404(Product, pk=pk, slug=url, is_active=True)
    return render(request, 'products/detail_product.html', {'product': product,
                                                            'form_product_form': form})
