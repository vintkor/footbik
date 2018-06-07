from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Club


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
