# Generated by Django 2.2.1 on 2019-05-05 09:58

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('brand', models.CharField(max_length=255, verbose_name='Brand')),
                ('size', models.CharField(max_length=255, verbose_name='size')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=product.models.product_feature_image_name, verbose_name='Featured Image - 100px x 100 px')),
                ('stock_level', models.IntegerField(blank=True, default=0, null=True, verbose_name='Stock Level')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]