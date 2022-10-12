from django.urls import reverse_lazy

from users.models import User
from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Название", max_length=70, unique=True)
    slug = models.SlugField("URL", unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'url': self.slug})


def upload_to(instance, filename):
    """Динамический путь для медиа файлов"""
    return f'products_images/{instance.category}/{instance.name}/{filename}'


class Product(models.Model):
    """Продукты"""
    name = models.CharField("Название", max_length=100)
    body = models.TextField("Краткое описание", max_length=256)
    description = models.TextField("Описание", blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='products')
    date_at = models.DateTimeField(auto_now_add=True)
    imag = models.ImageField(verbose_name='Картинка', upload_to=upload_to)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2, default=0)
    amount = models.PositiveSmallIntegerField("Количество на складе", default=0)
    is_active = models.BooleanField("В продаже", default=False)
    slug = models.SlugField('URL', unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail_product', kwargs={'url': self.slug, 'pk': self.pk})
