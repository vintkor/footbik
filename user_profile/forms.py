from django import forms
from django.utils.translation import ugettext as _
from user_profile.models import User

parent = 'parent'
investor = 'investor'

ROLE_CHOICE = (
    (parent, _('Родитель')),
    (investor, _('Инвестор')),
)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label=_('Пароль'))


class RegisterForm(forms.Form):
    first_name = forms.CharField(label=_('Имя'), required=False)
    last_name = forms.CharField(label=_('Фамилия'), required=False)
    email = forms.EmailField()
    role = forms.CharField(widget=forms.Select(choices=ROLE_CHOICE), label=_('Вы регистрируетесь как?'))
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label=_('Пароль'))
    password_repeat = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label=_('Повторить пароль'))

    def clean_password(self):
        not_allow_chars = (' ',)
        password = self.cleaned_data['password']
        if len(password) < 7:
            raise forms.ValidationError(_('Пароль должен быть больше 7 символов'), code='invalid')
        for char in password:
            if char in not_allow_chars:
                raise forms.ValidationError(_('Пароль не должен содержать символы пробела'), code='invalid')
        return password

    def get_password(self):
        return self.data.get('password')

    def clean_password_repeat(self):
        password_repeat = self.cleaned_data['password_repeat']
        password = self.get_password()

        if password != password_repeat:
            raise forms.ValidationError(_('Пароли не совпадают'), code='invalid')
        return password_repeat

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        is_email_in_db = User.objects.filter(email=email).exists()
        if is_email_in_db:
            raise forms.ValidationError(_('Пользователь с таким адресом уже существует'), code='invalid')
        return email

    def clean_role(self):
        role = self.cleaned_data['role']
        if role not in (parent, investor):
            raise forms.ValidationError(_('Вы должны выбрать только значение в этом списке!'), code='invalid')
        return role


class AddChildForm(forms.Form):
    first_name = forms.CharField(label=_('Имя'), required=False)
    last_name = forms.CharField(label=_('Фамилия'), required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label=_('Пароль'))
    password_repeat = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label=_('Повторить пароль'))

    def clean_password(self):
        not_allow_chars = (' ',)
        password = self.cleaned_data['password']
        if len(password) < 7:
            raise forms.ValidationError(_('Пароль должен быть больше 7 символов'), code='invalid')
        for char in password:
            if char in not_allow_chars:
                raise forms.ValidationError(_('Пароль не должен содержать символы пробела'), code='invalid')
        return password

    def get_password(self):
        return self.data.get('password')

    def clean_password_repeat(self):
        password_repeat = self.cleaned_data['password_repeat']
        password = self.get_password()

        if password != password_repeat:
            raise forms.ValidationError(_('Пароли не совпадают'), code='invalid')
        return password_repeat

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        is_email_in_db = User.objects.filter(email=email).exists()
        if is_email_in_db:
            raise forms.ValidationError(_('Пользователь с таким адресом уже существует'), code='invalid')
        return email
