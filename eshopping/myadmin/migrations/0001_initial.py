# Generated by Django 4.2 on 2023-04-17 11:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.BigIntegerField()),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=30)),
                ('date', models.DateField(default=datetime.date(2023, 4, 17))),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'inquiry',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(max_length=100)),
                ('rent', models.DecimalField(decimal_places=2, default='0.00', max_digits=5)),
                ('return_date', models.DateField(default=datetime.datetime.today)),
                ('penalty', models.DecimalField(decimal_places=2, default='0.00', max_digits=5)),
                ('refund', models.DecimalField(decimal_places=2, default='0.00', max_digits=5)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='myadmin.customer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='myadmin.customer')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Payment_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=30)),
                ('payment_id', models.TextField()),
                ('signature', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.order')),
            ],
            options={
                'db_table': 'Payment_Details',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.category')),
            ],
            options={
                'db_table': 'subcategory',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.order')),
                ('payment_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.payment_details')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.state')),
            ],
            options={
                'db_table': 'shipping',
            },
        ),
        migrations.CreateModel(
            name='Seller_Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.BigIntegerField()),
                ('address', models.TextField()),
                ('owner_name', models.CharField(max_length=30)),
                ('photo', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'seller_shop',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('t_type', models.CharField(max_length=20)),
                ('stock', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.category')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.customer')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.subcategory')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.customer')),
            ],
            options={
                'db_table': 'Order_details',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.state'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.state'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.order')),
                ('payment_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.payment_details')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.state')),
            ],
            options={
                'db_table': 'billing',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city'),
        ),
    ]
