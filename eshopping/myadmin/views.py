from django.shortcuts import render, redirect
from myadmin.models import *
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import render_to_string
from datetime import date
from django.conf import settings

def login(request):
    context = {}
    return render(request,'myadmin/login.html',context)

def dashboard(request):
  id = request.user.id
  result = User.objects.get(pk=id)
  context = {'result':result}
  return render(request, 'myadmin/dashboard.html', context)


def check_login(request):
  username  = request.POST['username']
  password  = request.POST['password']

  result = auth.authenticate(username=username, password=password)
  if result is None:
    print('Invalid UserName or Password')
    return redirect('/myadmin/')
                                                
  else: 
    if Customer.objects.filter(user_id=result.id).exists():
        messages.error(request, 'Invalid User..Try Again')
        return redirect('/myadmin/')

    elif Seller_Shop.objects.filter(user_id=result.id).exists():
        messages.error(request, 'Invalid User..Try Again')
        return redirect('/myadmin/')

    else:
        auth.login(request, result)
        return redirect('/myadmin/dashboard')

def logout(request):
  auth.logout(request)
  return redirect('/myadmin/')

def common_form(request):
    context = {}
    return render(request, 'myadmin/form.html',context)

def common_table(request):
    context = {}
    return render(request, 'myadmin/table.html',context)

# category views
def add_category(request):
    context = {}
    return render(request, 'myadmin/add_category.html',context)

def add_category_store(request):
    cat_name = request.POST['cat_name']
    print(cat_name)
    Category.objects.create(cat_name=cat_name)
    return redirect('/myadmin/add_category')

def delete_category(request,id):
    result = Category.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_categories')

def edit_category(request,id):
    result = Category.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/edit_category.html',context)

def update_category(request,id):
    cat_name = request.POST['cat_name']
    Category.objects.update_or_create(pk=id,defaults={'cat_name':cat_name})
    return redirect('/myadmin/all_categories')

def all_categories(request):
    result = Category.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_categories.html',context)

# subcategory views

def add_subcategory(request):
    result = Category.objects.all()
    context = {'categories':result}
    return render(request, 'myadmin/add_subcategory.html',context)

def add_subcategory_store(request):
    subcat_name = request.POST['subcat_name']
    cat_id = request.POST['cat_id']
  
    Subcategory.objects.create(subcat_name=subcat_name,category_id=cat_id)
    return redirect('/myadmin/add_subcategory')

def all_subcategories(request):
    result = Subcategory.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_subcategories.html',context)

def delete_subcategory(request,id):
    result = Subcategory.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_subcategories')

def edit_subcategory(request,id):
    result = Subcategory.objects.get(pk=id)
    categories = Category.objects.all()
    context = {'categories':categories,'result':result}
    return render(request, 'myadmin/edit_subcategory.html',context)

def update_subcategory(request,id):
    subcat_name = request.POST['subcat_name']
    cat_id = request.POST['cat_id']

    data = {
              'subcat_name' : subcat_name,
              'category_id':cat_id
           }
  
    Subcategory.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_subcategories')



# inquiry & feedback views

def inquiry(request):
    result = Inquiry.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/inquiry.html',context)

def feedback(request):
    result = Feedback.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/feedback.html',context)

def customers(request):
    result = Customer.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/customers.html',context)

def customer_details(request,id):
    result = Customer.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/customer_details.html',context)

def sellers(request):
    result = Seller_Shop.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/sellers.html',context)

# order views

def order(request):
    result = Order.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/order.html',context)

def order_details(request,id):
    result = Order_details.objects.filter(order_id=id)
    result2 = Payment_Details.objects.filter(order_id=id)
    result3 = Billing.objects.filter(order_id=id)
    result4 = Shipping.objects.filter(order_id=id)
    context = {'result':result,'result2':result2,'result4':result4,'result3':result3}
    return render(request, 'myadmin/order_details.html',context)

def shipping_billing(request,id):
    result3 = Billing.objects.get(order_id=id)
    result4 = Shipping.objects.get(order_id=id)
    context = {'result4':result4,'result3':result3}
    return render(request, 'myadmin/shipping_billing.html',context)

# Pie Chart

def demo(request):
    context = {}
    return render(request, 'myadmin/order.html',context)

#state, city and area
def add_state(request):
    context = {}
    return render(request, 'myadmin/add_state.html',context)

def store_state(request):
    name = request.POST['name']
    print(name)
    State.objects.create(state_name=name)
    return redirect('/myadmin/add_state')

def all_state(request):
    result = State.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_state.html',context)

def delete_state(request,id):
    result = State.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_state')

def edit_state(request,id):
    result = State.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/edit_state.html',context)

def update_state(request,id):
    name = request.POST['name']
    State.objects.update_or_create(pk=id,defaults={'state_name':name})
    return redirect('/myadmin/all_state')


def add_city(request):
    result = State.objects.all()
    context = {'states':result}
    return render(request, 'myadmin/add_city.html',context)

def store_city(request):
    name = request.POST['name']
    state_id = request.POST['state_id']
    print(name)
    City.objects.create(city_name=name,state_id=state_id)
    return redirect('/myadmin/add_city')

def all_city(request):
    result = City.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_city.html',context)

def delete_city(request,id):
    result = City.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_city')

def edit_city(request,id):
    result = City.objects.get(pk=id)
    states = State.objects.all()
    context = {'states':states,'result':result}
    return render(request, 'myadmin/edit_city.html',context)

def update_city(request,id):
    name = request.POST['name']
    state_id = request.POST['state_id']

    data = {
              'city_name' : name,
              'state_id':state_id
           }
  
    City.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_city')

def add_area(request):
    result2 = City.objects.all()
    context = {'cities':result2}
    return render(request, 'myadmin/add_area.html',context)

def store_area(request):
    name = request.POST['name']
    city_id = request.POST['city_id']
    Area.objects.create(area_name=name,city_id=city_id)
    return redirect('/myadmin/add_area')

def all_area(request):
    result = Area.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_area.html',context)

def delete_area(request,id):
    result = Area.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_area')

def edit_area(request,id):
    result = Area.objects.get(pk=id)
    cities = City.objects.all()
    context = {'cities':cities,'result':result}
    return render(request, 'myadmin/edit_area.html',context)

def update_area(request,id):
    name = request.POST['name']
    city_id = request.POST['city_id']

    data = {
              'area_name' : name,
              'city_id':city_id
           }
  
    Area.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_area')

def customer_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Customer.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':Customer.objects.all()}
    return render(request,'myadmin/customer_report.html',context)

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Customer.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('result.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


def order_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Order.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'all_order':result,'f':from_date,'t':to_date} 
        else:
            context = {'all_order':None} 
    else:
        context = {'all_order':Order.objects.all()}
    return render(request,'myadmin/order_report.html',context)

class GenerateOrderPdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Order.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('templates/temp.html', "w").write(render_to_string('order.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
