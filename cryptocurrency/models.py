from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import JSONField


class Currency(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
    code = models.CharField(max_length=7, verbose_name=_('Код'))
    course = models.DecimalField(decimal_places=7, max_digits=16, verbose_name=_('Курс'))
    is_active = models.BooleanField(default=False, verbose_name=_('Является активной'))

    class Meta:
        verbose_name = _('Валюта')
        verbose_name_plural = _('Валюты')

    def __str__(self):
        return self.code


class SystemSetting(models.Model):
    settings = JSONField(verbose_name=_('Настройки системы'))

    class Meta:
        verbose_name = _('Системные настройки')
        verbose_name_plural = _('Системные настройки')

    def __str__(self):
        return 'System settings data id json'
