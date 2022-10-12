# Generated by Django 4.1.2 on 2022-10-08 09:21

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='В продаже'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=12, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.TextField(max_length=256, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imag',
            field=models.ImageField(upload_to=products.models.upload_to, verbose_name='Картинка'),
        ),
    ]
