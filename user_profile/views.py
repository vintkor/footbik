from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    DetailView,
    FormView,
    ListView,
)
from .models import (
    User,
    Parent,
    Investor,
    Child,
)
from .forms import (
    LoginForm,
    RegisterForm,
    AddChildForm,
)
from django.contrib.auth import (
    logout,
    authenticate,
    login,
)
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth.mixins import LoginRequiredMixin


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    Профиль пользователя
    """
    context_object_name = 'user'
    template_name = 'user_profile/user-detail.html'

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('user:login'))


class LoginFormView(FormView):
    """
    Форма входа в кабинет
    """
    template_name = 'user_profile/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_active:
            return redirect(reverse('dashboard'))
        return super(LoginFormView, self).get(args, kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect(reverse_lazy('dashboard'))

        messages.error(self.request, _('Неверно введён логин или пароль'), extra_tags='danger')
        return redirect(reverse_lazy('user:login'))


class RegisterFormView(FormView):
    """
    Форма регистрации
    """
    template_name = 'user_profile/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if request.user.is_active:
            return redirect(reverse('dashboard'))
        return super(RegisterFormView, self).get(args, kwargs)

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        role_txt = form.cleaned_data['role']

        user = User()
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name

        if role_txt == 'parent':
            user.save()
            user.parent = Parent()
            user.parent.save()
        elif role_txt == 'investor':
            user.save()
            user.investor = Investor()
            user.investor.save()
        else:
            messages.error(self.request, _('Что то пошло не так'), extra_tags='danger')
            return redirect(reverse_lazy('user:register'))

        login(self.request, user)
        return redirect(reverse_lazy('dashboard'))


class ChildrenListView(ListView):
    """
    Список детей родителя
    """
    context_object_name = 'children'
    template_name = 'user_profile/my-children.html'

    def get_queryset(self):
        return Child.objects.select_related('user').filter(parent__user=self.request.user)


class AddChildFormView(FormView):
    """
    Форма добавления ребёнка
    """
    template_name = 'user_profile/add-child.html'
    form_class = AddChildForm

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = User()
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user.child = Child()
        user.child.parent = self.request.user.parent
        user.child.save()

        messages.success(self.request, _('Ребёнок успешно зарегистрирован'), extra_tags='success')
        return redirect(reverse_lazy('user:my-children'))
