from django.db import models
from django.utils.translation import ugettext as _
from geo.models import Region
from django.urls import reverse
from user_profile.models import User


class Club(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=230, unique=True)
    meta_keywords = models.CharField(max_length=200, verbose_name=_('META Ключевые слова'), blank=True, null=True)
    meta_description = models.CharField(max_length=200, verbose_name=_('META Описание'), blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_('Регион'))
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)
    super_admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Главный администратор клуба'))

    class Meta:
        verbose_name = _('Клуб')
        verbose_name_plural = _('Клубы')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news:detail', args=[self.slug])
