from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
    name = models.CharField(
        _('Название'),
        max_length=255,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )
    description = models.TextField(
        _('Описание'),
        max_length=500
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        order_insertion_by = ['name']


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('Категория'),

    )
    name = models.CharField(
        _('Название'),
        max_length=255
    )
    price = models.PositiveIntegerField(
        _('Цена')
    )
    quantity = models.PositiveIntegerField(
        _('Количество')
    )
    description = models.TextField(
        _('Описание'),
        max_length=500
    )
    image = models.ImageField(
        _('Изображение'),
        upload_to='product_images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Specification(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=100
    )
    value = models.CharField(
        _('Значение'),
        max_length=250
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Продукт'),
        related_name='specifications'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"

