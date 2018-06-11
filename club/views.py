import datetime
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from .models import (
    Club,
    Group,
    Schedule,
    ClubLesson,
)
from django.contrib import messages
from django.utils.translation import ugettext as _
from monthdelta import monthdelta


class ClubCabinetListView(ListView):
    """
    Список клубов в кабинете
    """
    template_name = 'club/club-cabinet-list.html'
    context_object_name = 'clubs'
    model = Club


class MyClubsCabinetListView(ListView):
    """
    Список клубов администратора
    """
    template_name = 'club/my-clubs-cabinet-list.html'
    context_object_name = 'clubs'

    def get_queryset(self):
        return Club.objects.filter(super_admin=self.request.user.administrator)


class ClubAdminActionsView(View):

    def get(self, request, club_id):
        club = Club.objects.get(pk=club_id)
        context = {
            'club': club,
        }
        return render(request, 'club/club-admin-start.html', context)


class GroupSchedulerView(View):
    """
    Расписание занятий группы
    """

    def get(self, request, club_id, group_id):
        club = Club.objects.get(id=club_id)
        group = Group.objects.get(id=group_id)

        context = {
            'club': club,
            'group': group,
        }

        return render(request, 'club/group-scheduler.html', context)

    def post(self, requets, club_id, group_id):
        events = Schedule.objects.filter(
            group_id=group_id,
        )
        events_list = []

        for item in events:
            events_list.append({
                'title': item.lesson.title,
                'start': item.date_start,
                'end': item.date_end,
                'color': item.group.color,
            })

        return JsonResponse(events_list, safe=False)


class ClubSchedulerView(View):
    """
    Расписание занятий клуба в целом
    """

    def get(self, request, club_id):
        club = Club.objects.get(id=club_id)

        context = {
            'club': club,
        }

        return render(request, 'club/club-scheduler.html', context)

    def post(self, requets, club_id):
        events = Schedule.objects.filter(group__club_id=club_id)
        events_list = []

        for item in events:
            events_list.append({
                'title': '{} ({})'.format(item.lesson.title, item.group.title),
                'start': item.date_start,
                'end': item.date_end,
                'color': item.group.color,
            })

        return JsonResponse(events_list, safe=False)


class AddScheduleEvent(View):
    """
    Добавление расписания занятий
    """

    def get(self, request, club_id):
        club = Club.objects.get(id=club_id)
        lessons = ClubLesson.objects.all()

        context = {
            'club': club,
            'lessons': lessons,
        }

        return render(request, 'club/partials/_add-schedule-event.html', context)

    def post(self, request, club_id):
        repeat = request.POST.get('repeater')

        group = get_object_or_404(Group, pk=request.POST.get('group'))
        lesson = get_object_or_404(ClubLesson, pk=request.POST.get('lesson'))
        date_start = datetime.datetime.strptime(request.POST.get('dateStart'), '%d.%m.%Y %H:%M')
        date_end = datetime.datetime.strptime(request.POST.get('dateEnd'), '%d.%m.%Y %H:%M')

        if date_start < date_end:
            days = ((date_start + monthdelta(int(repeat))) - date_start).days

            events = [
                Schedule(
                    group=group,
                    lesson=lesson,
                    date_start=date_start + datetime.timedelta(days=i),
                    date_end=date_end + datetime.timedelta(days=i),
                ) for i in range(0, int(days), 7)
            ]

            Schedule.objects.bulk_create(events)

            messages.success(request, _('Событие успешно добавлено'))
            return redirect(request.META.get('HTTP_REFERER'))

        messages.error(request, _('Дата начала не может быть больше даты завершения'), 'danger')
        return redirect(request.META.get('HTTP_REFERER'))
