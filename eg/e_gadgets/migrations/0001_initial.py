# Generated by Django 4.2 on 2023-04-12 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
                ('categoryDesc', models.CharField(max_length=100, null=True)),
                ('categoryStatus', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Comind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'comind',
            },
        ),
        migrations.CreateModel(
            name='customer_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=250)),
                ('pinCode', models.IntegerField()),
                ('isDefault', models.IntegerField()),
                ('city', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.city')),
            ],
            options={
                'db_table': 'customer_address',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('user', models.IntegerField()),
                ('vendor', models.IntegerField()),
                ('resolve', models.IntegerField()),
                ('createdAt', models.DateField()),
                ('vendorsAns', models.CharField(max_length=500)),
                ('adminAns', models.CharField(max_length=600)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('address', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.customer_address')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productPrice', models.FloatField()),
                ('productQty', models.IntegerField()),
                ('productImage', models.FileField(null=True, upload_to='upload/')),
                ('productDesc', models.CharField(max_length=500, null=True)),
                ('productStatus', models.BooleanField(default=True)),
                ('productColor', models.CharField(max_length=100, null=True)),
                ('productBrand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.brand')),
                ('productCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1)),
                ('contactnum', models.CharField(max_length=15)),
                ('createdAt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='vendor_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorName', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('pinCode', models.IntegerField()),
                ('contactNum', models.CharField(max_length=12)),
                ('customerSupportNumber', models.CharField(max_length=12)),
                ('feedbackEmail', models.CharField(max_length=30)),
                ('city', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.city')),
                ('state', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.state')),
                ('user', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.user')),
            ],
            options={
                'db_table': 'vendor_details',
            },
        ),
        migrations.CreateModel(
            name='vendor_product_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_product', models.IntegerField()),
                ('vendor', models.IntegerField()),
                ('imageUrl', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'vendor_product_images',
            },
        ),
        migrations.CreateModel(
            name='vendor_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('product', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.product')),
                ('vendor', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.vendor_details')),
            ],
            options={
                'db_table': 'vendor_product',
            },
        ),
        migrations.CreateModel(
            name='subCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoryName', models.CharField(max_length=30)),
                ('subcategoryStatus', models.BooleanField(default=True)),
                ('categoryName', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.category')),
            ],
            options={
                'db_table': 'subcategory',
            },
        ),
        migrations.CreateModel(
            name='order_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('order', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.order')),
                ('user', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.user')),
                ('vendor_product', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.vendor_product')),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.status'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.user'),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='state',
            field=models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.state'),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='user',
            field=models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.user'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.state'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('user', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.user')),
                ('vendorProduct', models.ForeignKey(max_length=9, on_delete=django.db.models.deletion.CASCADE, to='e_gadgets.vendor_product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]