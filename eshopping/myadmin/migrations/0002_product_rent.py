# Generated by Django 4.2 on 2023-04-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rent',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=5),
        ),
    ]
