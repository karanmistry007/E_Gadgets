# Generated by Django 4.2 on 2023-04-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_gadgets', '0002_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
