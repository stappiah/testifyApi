# Generated by Django 4.2.5 on 2023-11-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testify', '0012_alter_product_stock_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
