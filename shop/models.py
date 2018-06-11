from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


class Category(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name=_('Родитель'), null=True, blank=True,
        related_name='children', db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=230, unique=True)
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news:detail', args=[self.slug])


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=230, unique=True)
    image = models.ImageField(verbose_name=_('Главное изображение'), blank=True, null=True, upload_to='images/shop/')
    text = RichTextUploadingField(verbose_name=_('Текст'), blank=True, null=True)
    is_virtual = models.BooleanField(default=False, verbose_name=_('Является виртуальным товаром'))
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news:detail', args=[self.slug])


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_set')
    image = models.ImageField(verbose_name=_('Изображение'), upload_to='images/shop/')

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')

    def __str__(self):
        return self.product.title

    # def get_absolute_url(self):
    #     return reverse('news:detail', args=[self.slug])
