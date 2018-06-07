from django.urls import path, include
from .views import (
    ClubCabinetListView,
    MyClubsCabinetListView,
    ClubAdminActionsView,
)


app_name = 'club'
urlpatterns = [
    path('', ClubCabinetListView.as_view(), name='list-cabinet'),
    path('admin/', include([
        path('', MyClubsCabinetListView.as_view(), name='admin-my-clubs'),
        path('actions/<int:club_id>/', ClubAdminActionsView.as_view(), name='admin-club-actions'),
    ])),
]
