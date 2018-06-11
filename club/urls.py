from django.urls import path, include
from .views import (
    ClubCabinetListView,
    MyClubsCabinetListView,
    ClubAdminActionsView,
    GroupSchedulerView,
    ClubSchedulerView,
    AddScheduleEvent,
)


app_name = 'club'
urlpatterns = [
    path('', ClubCabinetListView.as_view(), name='list-cabinet'),
    path('admin/', include([
        path('', MyClubsCabinetListView.as_view(), name='admin-my-clubs'),
        path('actions/<int:club_id>/', ClubAdminActionsView.as_view(), name='admin-club-actions'),
        path('actions/<int:club_id>/scheduler/', ClubSchedulerView.as_view(), name='admin-club-scheduler'),
        path('actions/<int:club_id>/scheduler/add-event/', AddScheduleEvent.as_view(), name='admin-scheduler-add-event'),
        path('actions/<int:club_id>/scheduler/<int:group_id>/', GroupSchedulerView.as_view(), name='admin-group-scheduler'),
    ])),
]
