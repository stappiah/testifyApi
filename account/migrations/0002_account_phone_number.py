# Generated by Django 4.2.5 on 2023-09-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
