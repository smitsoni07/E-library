from django.db import models
from datetime import date
from django.contrib.auth.models import User
from datetime import datetime, date

class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name

    class Meta:
        db_table = 'category'

class Subcategory(models.Model):
    subcat_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategory'

class State(models.Model):
    state_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'state'

class City(models.Model):
    city_name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'

class Area(models.Model):
    area_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'area'

class Customer(models.Model):
    contact = models.BigIntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())

    class Meta:
        db_table = 'customer'


class Seller_Shop(models.Model):
    contact = models.BigIntegerField()
    address = models.TextField()
    owner_name = models.CharField(max_length=30)
    photo = models.CharField(max_length=255)
    about = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:         
        db_table = 'seller_shop'

class Product(models.Model):
    pname = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    quantity = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    t_type = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)
    rent = models.DecimalField(max_digits=5, decimal_places=2,default='0.00')
             
    class Meta:
        db_table = 'product' 

class Order(models.Model):
    amount = models.DecimalField(max_digits = 10,decimal_places = 2)
    buyer = models.ForeignKey(Customer, related_name='buyer' ,on_delete=models.CASCADE)
    seller = models.ForeignKey(Customer, related_name='seller' ,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=100)

    rent = models.DecimalField(max_digits=5, decimal_places=2,default='0.00')
    return_date = models.DateField(default=datetime.today)
    penalty = models.DecimalField(max_digits=5, decimal_places=2,default='0.00')
    refund = models.DecimalField(max_digits=5, decimal_places=2,default='0.00')

    class Meta:
        db_table = 'order'

class Order_details(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price  = models.DecimalField(max_digits = 10,decimal_places = 2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    seller  = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Order_details'

class Payment_Details(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=30)
    payment_id = models.TextField()
    signature = models.TextField()

    class Meta:
        db_table = 'Payment_Details'

class Inquiry(models.Model):
    name    = models.CharField(max_length=50)
    email   = models.EmailField()
    contact = models.BigIntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date    = models.DateField(default=date.today)

    class Meta:
        db_table = 'inquiry'

class Feedback(models.Model):
    rating = models.CharField(max_length=30)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        db_table = 'feedback'

class Cart(models.Model):
    quantity = models.BigIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'

class Billing(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.TextField()
    email = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_details = models.ForeignKey(Payment_Details, on_delete=models.CASCADE)


    class Meta:
        db_table = 'billing'

class Shipping(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.TextField()
    email = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_details = models.ForeignKey(Payment_Details, on_delete=models.CASCADE)

    class Meta:
        db_table = 'shipping'