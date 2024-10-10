# Generated by Django 5.1.1 on 2024-10-08 07:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_productcategory_product_stock_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='color',
            field=models.CharField(blank=True, choices=[('#ff3300', 'red'), ('#ffff00', 'Yellow'), ('#ff0066', 'pink')], help_text='Select color category', max_length=16, null=True, verbose_name='Color category'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]