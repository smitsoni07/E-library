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
from seller import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('common_form', views.common_form, name='common_form'),
    path('common_table', views.common_table, name='common_table'),
    path('', views.login, name='login'),
    path('add_product', views.add_product, name='add_product'),
    path('store_product', views.store_product, name='store_product'),
    path('all_products', views.all_products, name='all_products'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('order', views.order, name='order'),
    path('order_details/<int:id>', views.order_details, name='order_details'),
    path('shipping_billing/<int:id>', views.shipping_billing, name='shipping_billing'),
    path('check_login', views.check_login, name='check_login'),
    path('logout', views.logout, name='logout'),

    path('order_report', views.order_report, name='order_report'),
    path('pdf1/', views.GenerateOrderPdf.as_view()),

]
