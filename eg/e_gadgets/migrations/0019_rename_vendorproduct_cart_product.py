# Generated by Django 4.2 on 2023-04-17 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_gadgets', '0018_alter_cart_vendorproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='vendorProduct',
            new_name='Product',
        ),
    ]
