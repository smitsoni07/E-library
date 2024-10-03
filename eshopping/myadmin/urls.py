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
from myadmin import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('common_form', views.common_form, name='common_form'),
    path('common_table', views.common_table, name='common_table'),
   

    path('add_category', views.add_category, name='add_category'),
    path('add_category_store', views.add_category_store, name='add_category_store'),
    path('all_categories', views.all_categories, name='all_categories'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('update_category/<int:id>', views.update_category, name='update_category'),

    path('add_subcategory', views.add_subcategory, name='add_subcategory'),
    path('add_subcategory_store', views.add_subcategory_store, name='add_subcategory_store'),
    path('all_subcategories', views.all_subcategories, name='all_subcategories'),
    path('delete_subcategory/<int:id>', views.delete_subcategory, name='delete_subcategory'),
    path('edit_subcategory/<int:id>', views.edit_subcategory, name='edit_subcategory'),
    path('update_subcategory/<int:id>', views.update_subcategory, name='update_subcategory'),

    path('inquiry', views.inquiry, name='inquiry'),
    path('feedback', views.feedback, name='feedback'),
    path('customers', views.customers, name='customers'),
    path('customer_details/<int:id>', views.customer_details, name='customer_details'),
    path('sellers', views.sellers, name='sellers'),
    path('order', views.order, name='order'),
    path('order_details/<int:id>', views.order_details, name='order_details'),
    path('shipping_billing/<int:id>', views.shipping_billing, name='shipping_billing'),
    path('', views.login, name='login'),
    path('check_login', views.check_login, name='check_login'),
    path('logout', views.logout, name='logout'),

    path('add_state', views.add_state, name='add_state'),
    path('store_state', views.store_state, name='store_state'),
    path('all_state', views.all_state, name='all_state'),
    path('delete_state/<int:id>', views.delete_state, name='delete_state'),
    path('edit_state/<int:id>', views.edit_state, name='edit_state'),
    path('update_state/<int:id>', views.update_state, name='update_state'),

    path('add_city', views.add_city, name='add_city'),
    path('store_city', views.store_city, name='store_city'),
    path('all_city', views.all_city, name='all_city'),
    path('delete_city/<int:id>', views.delete_city, name='delete_city'),
    path('edit_city/<int:id>', views.edit_city, name='edit_city'),
    path('update_city/<int:id>', views.update_city, name='update_city'),

    path('add_area', views.add_area, name='add_area'),
    path('store_area', views.store_area, name='store_area'),
    path('all_area', views.all_area, name='all_area'),
    path('delete_area/<int:id>', views.delete_area, name='delete_area'),
    path('edit_area/<int:id>', views.edit_area, name='edit_area'),
    path('update_area/<int:id>', views.update_area, name='update_area'),

    path('customer_report', views.customer_report, name='customer_report'),
    path('order_report', views.order_report, name='order_report'),
    path('pdf/', views.GeneratePdf.as_view()),
    path('pdf1/', views.GenerateOrderPdf.as_view()),



]
