from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from myadmin.models import *
from django.contrib import auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from datetime import datetime, date
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import render_to_string
from datetime import date
from django.conf import settings


def dashboard(request):
    print(request.user.id)
    context = {}
    return render(request, 'seller/dashboard.html',context)

def common_form(request):
    context = {}
    return render(request, 'seller/form.html',context)

def common_table(request):
    context = {}
    return render(request, 'seller/table.html',context)

def login(request):
    context = {}
    return render(request, 'seller/login.html',context)

def check_login(request):
  username  = request.POST['username']
  password  = request.POST['password']

  result = auth.authenticate(username=username, password=password)
  if result is None:
    print('Invalid UserName or Password')
    return redirect('/seller/')

  else: 
    if Seller.objects.filter(user_id=result.id).exists():
        auth.login(request, result)
        return redirect('/seller/dashboard')

    elif Customer.objects.filter(user_id=result.id).exists():
        messages.error(request, 'Invalid User..Try Again')
        return redirect('/seller/')

    else:
        messages.error(request, 'Invalid User..Try Again')
        return redirect('/seller/')

def logout(request):
    auth.logout(request)
    return redirect('/seller/')

# product views

def add_product(request):
    categories = Category.objects.all()
    scategories = Subcategory.objects.all()
    context = {'categories':categories,'scategories':scategories}
    return render(request, 'seller/add_product.html',context)

def store_product(request):
    result = Seller.objects.get(user_id=request.user.id)

    pname = request.POST['pname']
    price = request.POST['price']
    quantity = request.POST['quantity']
    description = request.POST['description']

    image = request.FILES['image']
    myloc = os.path.join(settings.MEDIA_ROOT, 'product')
    obj = FileSystemStorage(location=myloc)
    obj.save(image.name, image)

    #checkbox
    psize = request.POST.getlist('ch[]')
    size = ','.join(psize)

    author = request.POST['author']

    category_id = request.POST['cat_id']
    subcategory_id = request.POST['sub_id']

    Product.objects.create(pname=pname,price=price,quantity=quantity,author=author,description=description,image=image.name,size=size,category_id=category_id,subcategory_id=subcategory_id,seller_id=result.id)
    return redirect('/seller/add_product')


def all_products(request):
    result = Product.objects.all()
    context = {'result':result}
    return render(request, 'seller/all_products.html',context)

def product_details(request,id):
    result = Product.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'seller/product_details.html', context)

def delete_product(request, id):
    result = Product.objects.get(pk=id)
    result.delete()

    return redirect('/seller/all_products')

def edit_product(request, id):
    result = Product.objects.get(pk=id)
    categories = Category.objects.all()
    scategories = Subcategory.objects.all()

    context = {'categories':categories,'scategories':scategories,'result':result}

    return render(request, 'seller/edit_product.html', context)

def update_product(request, id):
    result = Seller.objects.get(user_id=request.user.id)

    pname = request.POST['pname']
    price = request.POST['price']
    quantity = request.POST['quantity']
    description = request.POST['description']

    image = request.FILES['image']
    myloc = os.path.join(settings.MEDIA_ROOT, 'product')
    obj = FileSystemStorage(location=myloc)
    obj.save(image.name, image)

    #checkbox
    psize = request.POST.getlist('ch[]')
    size = ','.join(psize)

    category_id = request.POST['cat_id']
    subcategory_id = request.POST['sub_id']

    data = {
                'pname':pname,
                'price':price,
                'quantity':quantity,
                'description':description,
                'image':image.name,
                'size':size,
                'category_id':category_id,
                'subcategory_id':subcategory_id,
            }
    Product.objects.update_or_create(pk=id, defaults=data)
    return redirect('/seller/all_products')


# order views

def order(request):
    id = request.user.id
    seller = Seller.objects.get(user_id=id)
    result = Order.objects.filter(seller_id=seller.id)
    context = {'result':result}
    return render(request, 'seller/order.html',context)

def order_details(request,id):
    id1 = request.user.id
    result = Order_details.objects.filter(order_id=id)
    result2 = Payment_Details.objects.filter(order_id=id)
    result3 = Billing.objects.filter(order_id=id)
    result4 = Shipping.objects.filter(order_id=id)
    context = {'result':result,'result2':result2,'result4':result4,'result3':result3}
    return render(request, 'seller/order_details.html',context)

def shipping_billing(request,id):
    result3 = Billing.objects.get(order_id=id)
    result4 = Shipping.objects.get(order_id=id)
    context = {'result4':result4,'result3':result3}
    return render(request, 'seller/shipping_billing.html',context)




def order_report(request):
    id1 = request.user.id
    s_id = Seller.objects.get(user_id=id1)
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Order.objects.filter(date__gte=from_date,date__lte=to_date,seller_id=s_id)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'all_order':result,'f':from_date,'t':to_date} 
        else:
            context = {'all_order':None} 
    else:
        context = {'all_order':Order.objects.filter(seller_id=s_id)}
    return render(request,'seller/order_report.html',context)


class GenerateOrderPdf(View):
     def get(self, request, *args, **kwargs):
        id1 = request.user.id
        s_id = Seller.objects.get(user_id=id1)
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Order.objects.filter(date__gte=from_date,date__lte=to_date,seller_id=s_id)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('order.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')