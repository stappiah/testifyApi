# Generated by Django 3.2.1 on 2023-11-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testify', '0016_auto_20231122_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ManyToManyField(related_name='wishlists', to='testify.Product'),
        ),
    ]
