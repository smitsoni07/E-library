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
import razorpay
from django.views.decorators.csrf import csrf_exempt

def home(request):
    print(request.user.id)
    result = Category.objects.all()
    context = {'cat':result}
    return render(request, 'customer/home.html',context)

# account views

def login(request):
    context = {}
    return render(request, 'customer/login.html',context)

def check_login(request):
  username  = request.POST['username']
  password  = request.POST['password']

  result = auth.authenticate(username=username, password=password)
  if result is None:
    print('Invalid UserName or Password')
    return redirect('/customer/login')

  else: 
    if Customer.objects.filter(user_id=result.id).exists():
        auth.login(request, result)
        return redirect('/customer/home')

    elif Seller.objects.filter(user_id=result.id).exists():
        messages.error(request, 'Invalid User..Try Again')
        return redirect('/customer/login')

    else:
        messages.error(request, 'Invalid User..Try Again')
        return redirect('/customer/login')

def register(request):
    cities = City.objects.all()
    states = State.objects.all()
    areas = Area.objects.all()
    context = {'cities':cities, 'states':states,'areas':areas}
    return render(request, 'customer/register.html',context)

def store_user(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    email = request.POST['email']

    contact = request.POST['contact']
    address = request.POST['address']
    gender = request.POST['gender']
    state = request.POST['state']
    area = request.POST['area']
    city = request.POST['city']

    if password == cpassword:
        user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)

        Customer.objects.create(contact=contact,address=address,user_id=user.id,city_id=city,area_id=area,state_id=state,gender=gender)
        return redirect('/customer/login')

    else: 
        print('Password and confirm password mismatched')

def edit_profile(request):
    id = request.user.id
    result = Customer.objects.get(user_id=id)
    cities = City.objects.all()
    states = State.objects.all()
    areas = Area.objects.all()
    context = {'cities':cities, 'states':states,'areas':areas, 'result':result}
    return render(request, 'customer/edit_profile.html',context)

def update_profile(request):
    id = request.user.id
    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']

    contact = request.POST['contact']
    address = request.POST['address']
    gender = request.POST['gender']
    state = request.POST['state']
    area = request.POST['area']
    city = request.POST['city']

    data = {
        'first_name' : fname,
        'last_name' : lname,
        'email' : email,
        'username' : username
    }
    user = User.objects.update_or_create(pk=id,defaults=data)

    data2 = {
        'contact' : contact,
        'address' : address,
        'gender' : gender,
        'state_id' : state,
        'area_id' : area,
        'city_id' : city,
    }
    Customer.objects.update_or_create(user_id=id,defaults=data2)
    return redirect('/customer/home')

def change_password(request):
    id = request.user.id
    result = User.objects.get(pk=id)
    context = {'result' : result}
    return render(request, 'customer/change_password.html', context)

def spasse(request):
    username = request.user.username

    old_pass = request.POST['old_pass']
    new_pass = request.POST['new_pass']
    rnew_pass = request.POST['rnew_pass']

    if new_pass == rnew_pass:
        user = auth.authenticate(username=username,password=old_pass)
        if user is not None:
            user.set_password(new_pass)
            user.save()
            return redirect('/customer/login')
        else:
            messages.warning(request, 'Invalid password')
            print('Invalid Password')
        return redirect('/customer/change_password')

    else:
        messages.warning(request, 'Password and Confirm Password mismatched')    
        print('Password and Confirm Password mismatched')
        return redirect('/customer/change_password')

def logout(request):
    auth.logout(request)
    return redirect('/customer/login')


# common views

def about(request):
    context = {}
    return render(request, 'customer/about.html',context)

def contact(request):
    context = {}
    return render(request, 'customer/contact.html',context)

def contact_us(request):
    subject = request.POST['subject']
    message = request.POST['message']
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']


    Inquiry.objects.create(subject=subject,message=message,name=name,email=email,contact=contact)
    return redirect('/customer/home')


def cart(request):
    cus = Customer.objects.get(user_id=request.user.id)
    result = Cart.objects.filter(customer_id=cus.id)
    total_amount = 0

    for row in result:
        if row.product.t_type == 'rent':
            price_10 = float(row.product.price)*(10/100)
            row.total_rent = price_10 * row.quantity + float(row.product.price)
        
        else:
            total_amount = (row.product.price* row.quantity) + total_amount 
    s_total = 0
    for row in result:
        if row.product.t_type == 'rent':
            s_total = int(row.total_rent) + s_total
        else:
            s_total = (row.product.price * row.quantity) + s_total

    context = {'result':result,'total_amount':total_amount,'s_total':s_total}
    return render(request, 'customer/cart.html',context)

def add_cart(request, id):

    if request.user.is_authenticated:
        customer = Customer.objects.get(user_id=request.user.id)
        cart_data = Cart.objects.filter(product_id=id, customer_id=customer.id)
        if cart_data.exists():
            data = {
                     'quantity': cart_data[0].quantity + 1 
                  }
            Cart.objects.update_or_create(pk=cart_data[0].id, defaults=data)

        else:
            quantity = request.POST['quantity']
            Cart.objects.create(product_id=id,customer_id=customer.id,quantity=quantity)

       
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect('/customer/login')


def update_cart(request):
    cart_id = request.GET['cart_id']
    quantity = request.GET['quantity']

    data = {
             'quantity': quantity 
          }
    Cart.objects.update_or_create(pk=cart_id, defaults=data)
    return redirect('/customer/cart')

def place_order(request):
    cus = Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.filter(customer_id=cus.id)
    data = {'stock':'out'}
    method = request.POST['method']
    ship_bill = request.POST['ship_bill']

    if ship_bill == 'yes':
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        pin = request.POST['pin']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        area = request.POST['area']
        city = request.POST['city']

        sfname = request.POST['sfname']
        slname = request.POST['slname']
        saddress = request.POST['saddress']
        spin = request.POST['spin']
        semail = request.POST['semail']
        sphone = request.POST['sphone']
        sstate = request.POST['sstate']
        sarea = request.POST['sarea']
        scity = request.POST['scity']

        if method == 'online':
            total_amount = 0
            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                
                else:
                    total_amount = (row.product.price* row.quantity) + total_amount 
            s_total = 0
            for row in cart:
                if row.product.t_type == 'rent':
                    s_total = int(row.total_rent) + s_total
                else:
                    s_total = (row.product.price * row.quantity) + s_total

            order_info = Order.objects.create(amount=s_total,date=date.today(),status='pending',buyer_id=cus.id,seller_id=row.product.customer_id)

            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                    Order_details.objects.create(quantity=row.quantity,price=row.total_rent,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)
                else:
                    tprice = row.product.price*row.quantity
                    Order_details.objects.create(quantity=row.quantity,price=tprice,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)

            pd_info = Payment_Details.objects.create(payment_method='online',payment_id='p_id from razor pay',signature='sign_id from razor pay',order_id=order_info.id)
            Shipping.objects.create(fname=sfname,lname=slname,address=saddress,email=semail,phone=sphone,pin=spin,area_id=sarea,state_id=sstate,city_id=scity,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            Billing.objects.create(fname=fname,lname=lname,address=address,email=email,phone=phone,pin=pin,area_id=area,state_id=state,city_id=city,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            cart_clear = Cart.objects.filter(customer_id=cus.id)
            request.session['pd_id'] = pd_info.id 
            for update_data in cart:
                Product.objects.update_or_create(pk=update_data.product.id,defaults=data)

            cart_clear.delete()
            return redirect('/customer/make_payment')


        else:
            total_amount = 0
            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                
                else:
                    total_amount = (row.product.price* row.quantity) + total_amount 
            s_total = 0
            for row in cart:
                if row.product.t_type == 'rent':        
                    s_total = int(row.total_rent) + s_total
                else:
                    s_total = (row.product.price * row.quantity) + s_total

            order_info = Order.objects.create(amount=s_total,date=date.today(),status='pending',buyer_id=cus.id,seller_id=row.product.customer_id)

            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                    Order_details.objects.create(quantity=row.quantity,price=row.total_rent,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)
                else:
                    tprice = row.product.price*row.quantity
                    Order_details.objects.create(quantity=row.quantity,price=tprice,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)
            pd_info = Payment_Details.objects.create(payment_method='cod',payment_id='cod',signature='cod',order_id=order_info.id)
            Shipping.objects.create(fname=sfname,lname=slname,address=saddress,email=semail,phone=sphone,pin=spin,area_id=sarea,state_id=sstate,city_id=scity,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            Billing.objects.create(fname=fname,lname=lname,address=address,email=email,phone=phone,pin=pin,area_id=area,state_id=state,city_id=city,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            cart_clear = Cart.objects.filter(customer_id=cus.id)
            for update_data in cart:
                Product.objects.update_or_create(pk=update_data.product.id,defaults=data)
            cart_clear.delete()
            return redirect('/customer/success_payment')

    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        pin = request.POST['pin']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        area = request.POST['area']
        city = request.POST['city']

        if method == 'online':
            total_amount = 0
            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                
                else:
                    total_amount = (row.product.price* row.quantity) + total_amount 
            s_total = 0
            for row in cart:
                if row.product.t_type == 'rent':
                    s_total = int(row.total_rent) + s_total
                else:
                    s_total = (row.product.price * row.quantity) + s_total

            order_info = Order.objects.create(amount=s_total,date=date.today(),status='pending',buyer_id=cus.id,seller_id=row.product.customer_id)

            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                    Order_details.objects.create(quantity=row.quantity,price=row.total_rent,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)
                else:
                    tprice = row.product.price*row.quantity
                    Order_details.objects.create(quantity=row.quantity,price=tprice,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)
            pd_info = Payment_Details.objects.create(payment_method='online',payment_id='p_id from razor pay',signature='sign_id from razor pay',order_id=order_info.id)
            Shipping.objects.create(fname=fname,lname=lname,address=address,email=email,phone=phone,pin=pin,area_id=area,state_id=state,city_id=city,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            Billing.objects.create(fname=fname,lname=lname,address=address,email=email,phone=phone,pin=pin,area_id=area,state_id=state,city_id=city,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            cart_clear = Cart.objects.filter(customer_id=cus.id)
            request.session['pd_id'] = pd_info.id 
            for update_data in cart:
                Product.objects.update_or_create(pk=update_data.product.id,defaults=data)
            cart_clear.delete()
            return redirect('/customer/make_payment')

        else:
            total_amount = 0
            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                
                else:
                    total_amount = (row.product.price* row.quantity) + total_amount 
            s_total = 0
            for row in cart:
                if row.product.t_type == 'rent':
                    s_total = int(row.total_rent) + s_total
                else:
                    s_total = (row.product.price * row.quantity) + s_total

            order_info = Order.objects.create(amount=s_total,date=date.today(),status='pending',buyer_id=cus.id,seller_id=row.product.customer_id)

            for row in cart:
                if row.product.t_type == 'rent':
                    price_10 = float(row.product.price)*(10/100)
                    row.total_rent = price_10 * row.quantity + float(row.product.price)
                    Order_details.objects.create(quantity=row.quantity,price=row.total_rent,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)
                else:
                    tprice = row.product.price*row.quantity
                    Order_details.objects.create(quantity=row.quantity,price=tprice,order_id=order_info.id,product_id=row.product.id,seller_id=row.product.customer_id)
            pd_info = Payment_Details.objects.create(payment_method='cod',payment_id='cod',signature='cod',order_id=order_info.id)
            Shipping.objects.create(fname=fname,lname=lname,address=address,email=email,phone=phone,pin=pin,area_id=area,state_id=state,city_id=city,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            Billing.objects.create(fname=fname,lname=lname,address=address,email=email,phone=phone,pin=pin,area_id=area,state_id=state,city_id=city,order_id=order_info.id,payment_details_id=pd_info.id,customer_id=cus.id)
            cart_clear = Cart.objects.filter(customer_id=cus.id)
            for update_data in cart:
                Product.objects.update_or_create(pk=update_data.product.id,defaults=data)
            cart_clear.delete()
            return redirect('/customer/success_payment')

def make_payment(request):
    pd_id = request.session['pd_id']  
    key_id = 'rzp_test_qu1r85W33FbFlf'
    key_secret = 'mNX26pRh92aG5BqjlM9LIHLQ'

    cus = Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.filter(customer_id=cus.id)
    total_amount = 0
    for row in cart:
        if row.product.t_type == 'rent':
            price_10 = float(row.product.price)*(10/100)
            row.total_rent = price_10 * row.quantity + float(row.product.price)
        
        else:
            total_amount = (row.product.price* row.quantity) + total_amount 
    s_total = 0
    for row in cart:
        if row.product.t_type == 'rent':
            s_total = int(row.total_rent) + s_total
        else:
            s_total = (row.product.price * row.quantity) + s_total
    

    amount = s_total
    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': int(amount)*100,
        'currency': 'INR',
        "receipt":"BookBurter",
        "notes":{
            'name' : 'request.user.first_name',
            'payment_for':'Payment Test'
        }
    }

    data_pd = {'payment_id':'razorpay','signature':'razorpay'}
    phone = Customer.objects.get(user_id=request.user.id).contact
    payment = client.order.create(data=data)
    Payment_Details.objects.update_or_create(pk=pd_id,defaults=data_pd)
    context = {'payment' : payment,'total_amount':total_amount,'phone':phone,'s_total':s_total}
    return render(request, 'customer/process_payment.html',context)



@csrf_exempt
def r_details(request):
    pd_id = request.session['pd_id']


    order_id = request.POST.get('razorpay_order_id')
    payment_id = request.POST.get('razorpay_payment_id')
    signature = request.POST.get('razorpay_signature')
    client = razorpay.Client(auth=("rzp_test_qu1r85W33FbFlf", "mNX26pRh92aG5BqjlM9LIHLQ"))
    # print(client.utility.verify_payment_signature)
    
    try:
        client.utility.verify_payment_signature({
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        })
        print("Success")
        data_pd = {'payment_id':payment_id,'signature':signature}
        Payment_Details.objects.update_or_create(pk=pd_id,defaults=data_pd)
        # Maintenance_Payment.objects.create(order_id=order_id,payment_id=payment_id,signature=signature,date_time=datetime.today(),member_id=result,maintenance_id=id)
        # Payment is successful, do something here
        return redirect('/customer/success_payment')

    except:
        print("Failure") 
        # Payment failed, do something here



def remove_item(request,id):
    result = Cart.objects.get(pk=id)
    print(result.product.pname)
    result.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@csrf_exempt
def success_payment(request):
    context = {}
    return render(request, 'customer/success_payment.html',context)


def checkout(request):
    cus = Customer.objects.get(user_id=request.user.id)
    result = Cart.objects.filter(customer_id=cus.id)
    state = State.objects.all()
    city = City.objects.all()
    area = Area.objects.all()
    sub_total = 0
    for row in result:
        sub_total = (row.product.price* row.quantity) + sub_total 
        print(sub_total)


    total_amount = 0

    for row in result:
        if row.product.t_type == 'rent':
            price_10 = float(row.product.price)*(10/100)
            row.total_rent = price_10 * row.quantity + float(row.product.price)
        
        else:
            total_amount = (row.product.price* row.quantity) + total_amount 
    s_total = 0
    for row in result:
        if row.product.t_type == 'rent':
            s_total = int(row.total_rent) + s_total
        else:
            s_total = (row.product.price * row.quantity) + s_total



    context = {'result':result,'sub_total':sub_total,'state':state,'area':area,'city':city,'cus':cus,'s_total':s_total}
    return render(request, 'customer/checkout.html',context)

def product_details(request):
    context = {}
    return render(request, 'customer/product_details.html',context)

def product_list(request):
    context = {}
    return render(request, 'customer/product_list.html',context)

def seller(request):
    cities = City.objects.all()
    states = State.objects.all()
    areas = Area.objects.all()
    context = {'cities':cities, 'states':states,'areas':areas}
    return render(request, 'customer/seller.html',context)

def store_seller(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    email = request.POST['email']
    contact = request.POST['contact']
    address = request.POST['address']
    about = request.POST['about']

    image = request.FILES['photo']
    myloc = os.path.join(settings.MEDIA_ROOT, 'seller')
    obj = FileSystemStorage(location=myloc)
    obj.save(image.name, image)

    state = request.POST['state']
    area = request.POST['area']
    city = request.POST['city']

    if password == cpassword:
        user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)

        Seller.objects.create(contact=contact,address=address,user_id=user.id,photo=image.name,city_id=city,area_id=area,state_id=state,owner_name=fname+lname,about=about)
        return redirect('/seller')

    else:
        print('Password and confirm password mismatched')


def all_books(request):
    result = Product.objects.all()
    context = {'result':result}

    return render(request, 'customer/all_books.html', context)

def book_details(request, id):
    result = Product.objects.get(pk=id)
    r2 = Product.objects.order_by('id').reverse()[:5]
    print(r2)
    context = {'result':result,'r2':r2}

    return render(request, 'customer/book_details.html', context)

def books(request,id):
    if request.method == 'POST':
        ttype = request.POST['t_type']
        tttype = ttype
        if ttype == 'buy':
            ttype = 'sell'
        result = Product.objects.filter(t_type=ttype)

    else:
        result = Product.objects.filter(category_id=id)
        tttype = ''
    cname = Category.objects.get(pk=id)
    sname = Subcategory.objects.all()
    cnameall = Category.objects.all()
    context = {'result':result,'cname':cname,'snameall':sname,'cnameall':cnameall, 'tttype':tttype}

    return render(request, 'customer/books.html', context) 


def feedback(request):
    context = {}
    return render(request,'customer/feedback.html', context)

def feedback_store(request):
    rating = request.POST['rating']
    comment = request.POST['comment']
    
    Feedback.objects.create(rating=rating,comment=comment,user_id=request.user.id,date=date.today())
    return redirect('/customer/home')

def add_book(request):
    categories = Category.objects.all()
    scategories = Subcategory.objects.all()
    context = {'categories':categories,'scategories':scategories}
    return render(request, 'customer/add_book.html',context)

def store_book(request):
    result = Customer.objects.get(user_id=request.user.id)

    pname = request.POST['pname']
    price = request.POST['price']
    quantity = request.POST['quantity']
    description = request.POST['description']

    image = request.FILES['image']
    myloc = os.path.join(settings.MEDIA_ROOT, 'product')
    obj = FileSystemStorage(location=myloc)
    obj.save(image.name, image)

    author = request.POST['author']

    category_id = request.POST['cat_id']
    subcategory_id = request.POST['sub_id']
    t_type = request.POST['t_type']

    if t_type == 'rent':
        rent = int(price)/10
        Product.objects.create(rent=rent,pname=pname,t_type=t_type,price=price,stock="in",quantity=quantity,author=author,description=description,image=image.name,category_id=category_id,subcategory_id=subcategory_id,customer_id=result.id)

    else:
        Product.objects.create(pname=pname,t_type=t_type,price=price,stock="in",quantity=quantity,author=author,description=description,image=image.name,category_id=category_id,subcategory_id=subcategory_id,customer_id=result.id)
    return redirect('/customer/add_book')


def sbooks(request,id):
    if request.method == 'POST':
        ttype = request.POST['t_type']
        tttype = ttype
        if ttype == 'buy':
            ttype = 'sell'
        result = Product.objects.filter(t_type=ttype)

    else:
        result = Product.objects.filter(category_id=id)
        tttype = ''
    cname = Category.objects.get(pk=id)
    sname = Subcategory.objects.all()
    cnameall = Category.objects.all()
    context = {'result':result,'cname':cname,'snameall':sname,'cnameall':cnameall, 'tttype':tttype}

    return render(request, 'customer/books.html', context) 

def my_products(request):
    customer_details = Customer.objects.get(user_id=request.user.id)
    result = Product.objects.filter(customer_id=customer_details.id)

    context = {'result':result}
    return render(request, 'customer/my_products.html',context)

def delete_product(request, id):
    result = Product.objects.get(pk=id)
    result.delete()
    print(result.pname)
    return redirect('/customer/my_products')


def edit_product(request, id):
    result = Product.objects.get(pk=id)
    categories = Category.objects.all()
    scategories = Subcategory.objects.all()

    context = {'categories':categories,'scategories':scategories,'result':result}

    return render(request, 'customer/edit_product.html', context)

def update_product(request, id):
    result = Customer.objects.get(user_id=request.user.id)

    pname = request.POST['pname']
    price = request.POST['price']
    quantity = request.POST['quantity']
    description = request.POST['description']

    image = request.FILES['image']
    myloc = os.path.join(settings.MEDIA_ROOT, 'product')
    obj = FileSystemStorage(location=myloc)
    obj.save(image.name, image)

    author = request.POST['author']

    category_id = request.POST['cat_id']
    subcategory_id = request.POST['sub_id']
    t_type = request.POST['t_type']

    data ={
        'pname':pname,
        'price':price,
        'description':description,
        'image':image.name,
        'author':author,
        'category_id':category_id,
        'subcategory_id':subcategory_id,
    }
    Product.objects.update_or_create(pk=id, defaults=data)
    return redirect('/customer/my_products')


def orders(request):
    c_id = Customer.objects.get(user_id=request.user.id)
    result = Order.objects.filter(buyer_id=c_id.id)
    context = {'result':result}

    return render(request,'customer/orders.html', context)

def selling_orders(request):
    c_id = Customer.objects.get(user_id=request.user.id)
    result = Order.objects.filter(seller_id=c_id.id)
    context = {'result':result}

    return render(request,'customer/selling_orders.html', context)

def order_details(request,id):
    result = Order_details.objects.filter(order_id=id)
    context = {'result':result}

    return render(request, 'customer/order_details.html', context)

def selling_details(request,id):
    result = Order_details.objects.filter(order_id=id)
    context = {'result':result}

    return render(request, 'customer/selling_details.html', context)

def return_book(request,id):
    state = State.objects.all()
    city = City.objects.all()
    area = Area.objects.all()
    cus = Customer.objects.get(user_id=request.user.id)
    result = Order_details.objects.get(pk=id)
    result2 = Product.objects.get(pk=result.product.id)

    order_date = result.order.date
    today_date = date.today()
    d1 = datetime.strptime(str(order_date), "%Y-%m-%d")
    d2 = datetime.strptime(str(today_date), "%Y-%m-%d")
    diff = d2-d1
    difference = diff.days-30
    amount_refund = result2.price
    deposite = result2.price

    total_penalty = 0
    if diff.days>30:
        rent_per_day = result2.rent/30
        total_penalty = rent_per_day*difference*2
        total_penalty = round(total_penalty,2)
        amount_refund = amount_refund - total_penalty
    total_rent = result2.rent * result.quantity
    data2 = {'stock':'in'}
    data = {'penalty':total_penalty,'refund':amount_refund,'rent':total_rent,'return_date':date.today()}
    Product.objects.update_or_create(pk=result2.id,defaults=data2)
    Order.objects.update_or_create(pk=result.order_id,defaults=data)
    context = {'result':result,'state':state,'area':area,'city':city,'result2':result2,'diff':difference,'deposite':deposite,'cus':cus,'total_penalty':total_penalty,'amount_refund':amount_refund}
    return render(request, 'customer/return_book.html', context)

def store_return(request,id):
    cus = Customer.objects.get(user_id=request.user.id)
    result = Order_details.objects.get(pk=id)
    result2 = Product.objects.get(pk=result.product.id)

    order_date = result.order.date
    today_date = date.today()
    d1 = datetime.strptime(str(order_date), "%Y-%m-%d")
    d2 = datetime.strptime(str(today_date), "%Y-%m-%d")
    diff = d2-d1
    difference = diff.days-30
    amount_refund = result2.price
    deposite = result2.price

    total_penalty = 0
    if diff.days>30:
        rent_per_day = result2.rent/30
        total_penalty = rent_per_day*difference*2
        total_penalty = round(total_penalty,2)
        amount_refund = amount_refund - total_penalty
    total_rent = result2.rent * result.quantity
    data2 = {'stock':'in','status':'returned'}
    data = {'penalty':total_penalty,'refund':amount_refund,'rent':total_rent,'return_date':date.today()}
    Product.objects.update_or_create(pk=result2.id,defaults=data2)
    Order.objects.update_or_create(pk=result.order_id,defaults=data)
    return redirect('/customer/orders')