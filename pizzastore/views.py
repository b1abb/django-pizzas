from django.shortcuts import render, get_object_or_404, redirect

from review.forms import ReviewForm
from review.models import Review
from .forms import PizzaForm
from .models import Pizza
from category.models import Category
from checkout.models import order_list
from checkout.models import order
from checkout.models import invoice
from accounts.models import Account
from checkout.models import invoice
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render

categories_list = Category.objects.all()


# adding paging

def index(request):
    return render(request, 'index.html')


def home(request):
    pizzas = Pizza.objects.all()[0:20]
    font_page_context = {
        'pizzas': pizzas,
    }
    return render(request, 'index.html', font_page_context)


def contact(request):
    return render(request, 'contact-us.html')


def about(request):
    return render(request, 'about.html')


def single_pizza(request, single_pizza_slug):
    if single_pizza_slug is not None:
        pizza = get_object_or_404(Pizza, slug=single_pizza_slug)
        related_pizzas = Pizza.objects.filter(category=pizza.category).exclude(id=pizza.id)[:5]

        # Получаем параметр сортировки из GET-запроса
        sort_by = request.GET.get('sort', 'date')

        if sort_by == 'rating':
            reviews = Review.objects.filter(pizza=pizza).order_by('-rating')
        else:
            reviews = Review.objects.filter(pizza=pizza).order_by('-created_on')

        if request.method == 'POST':
            if request.user.is_authenticated:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.pizza = pizza
                    review.user = request.user
                    review.save()
                    return redirect('single_pizza', single_pizza_slug=single_pizza_slug)
            else:
                return redirect('login')
        else:
            form = ReviewForm()

        context = {
            'pizza': pizza,
            'related_pizzas': related_pizzas,
            'reviews': reviews,
            'form': form,
            'sort_by': sort_by,
        }

    return render(request, 'pizza-single-page.html', context)


def search_result(request):
    if 'query' in request.GET:
        q = request.GET['query']
        pizzas = Pizza.objects.all().filter(title=q)
        print(q)
        print(pizzas)
        context = {
            'pizzas': pizzas,
        }
        return render(request, 'search_res.html', context)


@login_required(login_url="/login")
def orders(request):
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)
        order_id = order.objects.all().filter(client=user).order_by('date_created')

        all_orders = Paginator(order.objects.all().filter(client=user).order_by('-date_created'), 10)
        page = request.GET.get('page')

        try:
            orders = all_orders.page(page)
        except PageNotAnInteger:
            orders = all_orders.page(1)
        except EmptyPage:
            orders = all_orders.page(all_orders.num_pages)

        context = {

            'order_id_list': orders,
        }
        return render(request, "list-orders.html", context)
    else:
        messages.error("Sorry, you need to be logged in to view your orders")
        return redirect("login")


@login_required(login_url="/login")
def view_order(request, order_id):
    if request.user.is_authenticated:

        print(order_id)
        order_items_list = order_list.objects.all().filter(order_id=order_id)
        invoice_details = invoice.objects.all().filter(order_id=order_id)

        context = {
            "order_id": order_id,

            "order_items_list": order_items_list,
            "invoice_list": invoice_details
        }
        return render(request, "view_order.html", context=context)
    else:
        return redirect('login')


@login_required(login_url="/login")
def view_invoice(request, invoice_id):
    if request.user.is_authenticated:
        invoice_dat = invoice.objects.get(invoice_id=invoice_id)

        context = {

            'invoice': invoice_dat

        }
        return render(request, "view_invoice.html", context=context)
    else:
        return redirect("login")


def is_admin(user):
    return user.is_staff


@login_required(login_url="/login")
@user_passes_test(is_admin, login_url="/login")
def product_list(request):
    products = Pizza.objects.all()
    return render(request, 'product-list.html', {'products': products})


@login_required(login_url="/login")
@user_passes_test(is_admin, login_url="/login")
def add_product(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно добавлен.')
            return redirect('product_list')
    else:
        form = PizzaForm()
    categories = Category.objects.all()
    return render(request, 'add_edit_product.html', {'form': form, 'edit': False, 'categories': categories})


@login_required(login_url="/login")
@user_passes_test(is_admin, login_url="/login")
def edit_product(request, product_id):
    product = get_object_or_404(Pizza, id=product_id)
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно обновлен.')
            return redirect('product_list')
    else:
        form = PizzaForm(instance=product)
    categories = Category.objects.all()
    return render(request, 'add_edit_product.html', {'form': form, 'edit': True, 'categories': categories})


@login_required(login_url="/login")
@user_passes_test(is_admin, login_url="/login")
def delete_product(request, product_id):
    product = get_object_or_404(Pizza, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Продукт успешно удален.')
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})
