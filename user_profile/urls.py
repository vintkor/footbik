from django.urls import path, include
from .views import (
    UserDetailView,
    LoginFormView,
    logout_view,
    RegisterFormView,
    ChildrenListView,
    AddChildFormView,
    EditProfileFormView,
)


app_name = 'user'
urlpatterns = [
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/edit/', EditProfileFormView.as_view(), name='edit-profile'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('parent/', include([
        path('my-children/', ChildrenListView.as_view(), name='my-children'),
        path('add-child/', AddChildFormView.as_view(), name='add-child'),
    ])),
]
