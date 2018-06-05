from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from footbik import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include([
        path('', TemplateView.as_view(template_name='cabinet.html'), name='dashboard'),
        path('user/', include('user_profile.urls')),
    ])),
    path('', TemplateView.as_view(template_name='publick.html'), name='index'),
    path('news/', include('news.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
