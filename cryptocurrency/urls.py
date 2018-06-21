from django.urls import path, include
from .views import (
    IcoIndexView,
    BuyView,
)


app_name = 'cryptocurrency'
urlpatterns = [
    path('', IcoIndexView.as_view(), name='index'),
    path('buy/', BuyView.as_view(), name='buy'),
]
