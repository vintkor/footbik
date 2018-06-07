from django.db import models
from django.utils.translation import ugettext as _
from club.models import Group, ClubLesson


class Schedule(models.Model):
    """
    Расписание занятий
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lesson = models.ForeignKey(ClubLesson, on_delete=models.CASCADE)
    date_start = models.DateTimeField(verbose_name=_('Начало занятия'))
    date_end = models.DateTimeField(verbose_name=_('Завершение занятия'))

    class Meta:
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписания')

    def __str__(self):
        return '{} - {} с {} до {}'.format(
            self.group,
            self.lesson,
            self.date_start,
            self.date_end,
        )
