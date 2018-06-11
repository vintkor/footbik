from django.db import models
from django.utils.translation import ugettext as _
from geo.models import Region
from django.urls import reverse
from user_profile.models import User, Administrator, Child
from colorfield.fields import ColorField


class Club(models.Model):
    """
    Модель клуба
    """
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    slug = models.SlugField(null=True, max_length=230, unique=True)
    meta_keywords = models.CharField(max_length=200, verbose_name=_('META Ключевые слова'), blank=True, null=True)
    meta_description = models.CharField(max_length=200, verbose_name=_('META Описание'), blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_('Регион'))
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)
    super_admin = models.ForeignKey(Administrator, on_delete=models.CASCADE, verbose_name=_('Главный администратор клуба'))

    class Meta:
        verbose_name = _('Клуб')
        verbose_name_plural = _('Клубы')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news:detail', args=[self.slug])


class ClubAdministrator(models.Model):
    """
    Администраторы клуба
    """
    user = models.ForeignKey(User, verbose_name=_('Пользователь'), on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Администратор клуба')
        verbose_name_plural = _('Администраторы клубов')

    def __str__(self):
        return self.user


class ClubImage(models.Model):
    """
    Изображение клуба
    """
    image = models.ImageField(verbose_name=_('Изображение'), upload_to='media/images/clubs/')
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'), blank=True, null=True)
    alt = models.CharField(max_length=200, blank=True, null=True)
    sort = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(verbose_name=_('Дата создания'), auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = _('Изображение клуба')
        verbose_name_plural = _('Изображения клубов')
        ordering = ('sort',)

    def __str__(self):
        return self.title if self.title else self.image.url


class ClubLesson(models.Model):
    """
    Занятие клуба
    """
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    description = models.CharField(max_length=200, verbose_name=_('META Описание'), blank=True, null=True)
    is_test = models.BooleanField(default=False, verbose_name=_('Пробное занятие'))

    class Meta:
        verbose_name = _('Урок')
        verbose_name_plural = _('Уроки')

    def __str__(self):
        return self.title


class Group(models.Model):
    """
    Группа (класс) клуба
    """
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    children = models.ManyToManyField(Child)
    color = ColorField(verbose_name=_('Цвет'), default='#238a53')

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')

    def __str__(self):
        return self.title

    def count_children(self):
        return self.children.count()


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
