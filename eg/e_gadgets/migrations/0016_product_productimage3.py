# Generated by Django 4.2 on 2023-04-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_gadgets', '0015_product_productimage2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage3',
            field=models.FileField(null=True, upload_to='upload1/'),
        ),
    ]