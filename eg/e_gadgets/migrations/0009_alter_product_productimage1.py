# Generated by Django 4.2 on 2023-04-14 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_gadgets', '0008_alter_brand_brandstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage1',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]