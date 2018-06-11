from django.db import models
from django.utils.translation import ugettext as _
from geo.models import Region
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=230, unique=True)
    meta_keywords = models.CharField(max_length=200, verbose_name=_('META Ключевые слова'), blank=True, null=True)
    meta_description = models.CharField(max_length=200, verbose_name=_('META Описание'), blank=True, null=True)
    region = models.ForeignKey(Region, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(verbose_name=_('Изображение'), upload_to='images/news/')
    excerpt = models.TextField(verbose_name=_('Анонс'))
    text = RichTextUploadingField(verbose_name=_('Текст'))
    created = models.DateTimeField(verbose_name=_('Дата создания'))

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', args=[self.slug])
