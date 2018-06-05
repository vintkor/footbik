from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ClubConfig(AppConfig):
    name = 'club'
    verbose_name = _('Клуб')
