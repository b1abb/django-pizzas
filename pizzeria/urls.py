"""
URL configuration for pizzeria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pizzastore.views import home, product_list, add_product, edit_product, delete_product
from pizzastore.views import contact
from pizzastore.views import about
from django.conf.urls.static import static
from django.conf import settings
from category.views import category
from pizzastore.views import single_pizza
from cart.views import add_to_cart
from cart.views import cart
from cart.views import delete_cart_item
from cart.views import update_cart_item
from pizzastore.views import search_result
from accounts.views import register
from accounts.views import login
from accounts.views import logout
from accounts.views import account_home
from checkout.views import checkout_req, checkout_page
from pizzastore.views import orders
from pizzastore.views import view_order
from pizzastore.views import view_invoice
from accounts.views import profile_edit
from accounts.views import change_pwd

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('feedback/', include('feedback.urls')),
                  path('', home, name="home"),
                  path('contact', contact),
                  path('about', about),
                  path('category/<slug:cat_slug>/', category),
                  path('category/', category),
                  path('pizza/<slug:single_pizza_slug>/', single_pizza, name='single_pizza'),
                  path('cart/', cart, name='cart'),
                  path('add_to_cart/<str:user_book>', add_to_cart, name="add_cart"),
                  path('update_cart_item/<str:book_slug>', update_cart_item, name="update_cart"),
                  path('delete_cart_item/<str:book_slug>', delete_cart_item, name="delete_cart_item"),
                  path('search/', search_result, name="search_res"),
                  path('register', register, name="register"),
                  path('login', login, name="login"),
                  path('logout', logout, name="logout"),
                  path('checkout', checkout_page, name="checkout_page"),
                  path('checkout_req/process', checkout_req, name="checkout_req"),
                  path("dashboard/", account_home, name="dashboard"),
                  path('dashboard/orders', orders, name="orders"),
                  path('dashboard/profile_edit', profile_edit, name="profile_edit"),
                  path("dashboard/view_order/<int:order_id>", view_order, name="view_order"),
                  path("dashboard/view_invoice/<int:invoice_id>", view_invoice, name="view_invoice"),
                  path('dashboard/change_pwd', change_pwd, name="change_pwd"),
                  path('dashboard/product_list', product_list, name="product_list"),
                  path('dashboard/add_product', add_product, name='add_product'),
                  path('dashboard/edit_product/<int:product_id>', edit_product, name='edit_product'),
                  path('dashboard/delete_product/<int:product_id>', delete_product, name='delete_product'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
