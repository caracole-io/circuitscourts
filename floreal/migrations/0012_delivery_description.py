# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 09:23


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floreal', '0011_product_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('place', '-quantity_per_package', 'name')},
        ),
        migrations.AddField(
            model_name='delivery',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
