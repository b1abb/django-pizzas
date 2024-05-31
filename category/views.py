from django.shortcuts import render,get_object_or_404
from pizzastore.models import Pizza
from .models import Category
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from category.models import Category



def category(request, cat_slug=None):
    cat_name = ""
    if cat_slug is None:
        all_books = Paginator(Pizza.objects.all().order_by('-modified_on'),20)
    else:
        print(cat_slug)
        cat = Category.objects.get(slug=cat_slug)
        all_books = Paginator(Pizza.objects.all().filter(category=cat).order_by('-modified_on'),20)
        cat_name= cat.category_name

    page = request.GET.get('page')

    try:
        pizzas = all_books.page(page)
    except PageNotAnInteger:
        pizzas = all_books.page(1)
    except EmptyPage:
        pizzas = all_books.page(1)

    context = {
        'pizzas': pizzas,
         'category_name':cat_name,
    }
    return render(request, 'pizzas-cat.html', context)


