# Generated by Django 3.2.1 on 2023-11-23 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testify', '0018_auto_20231123_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
