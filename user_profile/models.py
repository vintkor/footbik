from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=255, unique=True, db_index=True)
    avatar = models.ImageField('Аватар', blank=True, null=True, upload_to="user/avatar")
    first_name = models.CharField(_('Фамилия'), max_length=40, null=True, blank=True)
    last_name = models.CharField(_('Имя'), max_length=40, null=True, blank=True)
    date_of_birth = models.DateField(_('Дата рождения'), null=True, blank=True)
    is_active = models.BooleanField(_('Активен'), default=True)
    is_admin = models.BooleanField(_('Суперпользователь'), default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Дата создания'))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('Дата обновления'))

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def is_parent(self):
        if self.parent:
            return True
        return False

    def is_investor(self):
        if self.investor:
            return True
        return False

    def is_child(self):
        if self.child:
            return True
        return False

    def is_administrator(self):
        if self.administrator:
            return True
        return False


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # TODO Добавить адрес пользователя в смарте

    class Meta:
        verbose_name = _('Инвестор')
        verbose_name_plural = _('Инвесторы')

    def __str__(self):
        return self.user.get_full_name()


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # TODO Добавить адрес пользователя в смарте

    class Meta:
        verbose_name = _('Родитель')
        verbose_name_plural = _('Родители')

    def __str__(self):
        return self.user.get_full_name()


class Child(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Ребёнок')
        verbose_name_plural = _('Дети')

    def __str__(self):
        return self.user.get_full_name()


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Администратор клуба')
        verbose_name_plural = _('Администраторы клубов')

    def __str__(self):
        return self.user.get_full_name()
