from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _


class Region(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name=_('Родитель'), null=True, blank=True,
        related_name='children', db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=170, unique=True)
    code = models.CharField(max_length=15, blank=True, null=True, unique=True, verbose_name=_('Код региона'))

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = _('Регион')
        verbose_name_plural = _('Регионы')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('catalog-category', args=[self.slug])
