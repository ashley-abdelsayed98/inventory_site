# Generated by Django 4.0.1 on 2022-01-20 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_rename_item_product_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
        migrations.RenameField(
            model_name='warehouseinventory',
            old_name='product',
            new_name='item',
        ),
    ]
