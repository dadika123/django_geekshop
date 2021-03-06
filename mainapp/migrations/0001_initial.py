# Generated by Django 2.2 on 2021-02-28 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Категория Продукта',
                'verbose_name_plural': 'Категории Продуктов',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]