"""webcourt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from customer import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('check_login', views.check_login, name='check_login'),
    path('store_user', views.store_user, name='store_user'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('cart', views.cart, name='cart'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('update_cart', views.update_cart, name='update_cart'),
    path('remove_item/<int:id>', views.remove_item, name='remove_item'),
    path('checkout', views.checkout, name='checkout'),
    path('product_details', views.product_details, name='product_details'),
    path('product_list', views.product_list, name='product_list'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('spasse', views.spasse, name='spasse'),
    path('logout', views.logout, name='logout'),
    path('seller', views.seller, name='seller'),
    path('store_seller', views.store_seller, name='store_seller'),
    path('all_books', views.all_books, name='all_books'),
    path('book_details/<int:id>', views.book_details, name='book_details'),
    path('sbooks/<int:id>', views.sbooks, name='sbooks'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('order_details/<int:id>', views.order_details, name='order_details'),
    path('selling_details/<int:id>', views.selling_details, name='selling_details'),
    path('store_return/<int:id>', views.store_return, name='store_return'),
    path('return_book/<int:id>', views.return_book, name='return_book'),
    path('books/<int:id>', views.books, name='books'),
    path('place_order', views.place_order, name='place_order'),
    path('success_payment', views.success_payment, name='success_payment'),
    path('make_payment', views.make_payment, name='make_payment'),
    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('r_details', views.r_details, name='r_details'),
    path('add_book', views.add_book, name='add_book'),
    path('store_book', views.store_book, name='store_book'),
    path('my_products', views.my_products, name='my_products'),
    path('orders', views.orders, name='orders'),
    path('selling_orders', views.selling_orders, name='selling_orders'),
]
