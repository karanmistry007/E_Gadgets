# Generated by Django 4.2 on 2023-04-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_gadgets', '0011_addfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage2',
            field=models.FileField(null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productImage1',
            field=models.FileField(null=True, upload_to='upload/'),
        ),
    ]