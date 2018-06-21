from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from footbik import settings
from footbik.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include([
        path('', TemplateView.as_view(template_name='cabinet.html'), name='dashboard'),
        path('user/', include('user_profile.urls')),
        path('club/', include('club.urls')),
        path('shop/', include('shop.urls')),
        path('cryptocurrency/', include('cryptocurrency.urls')),
    ])),
    path('', TemplateView.as_view(template_name='publick.html'), name='index'),
    path('news/', include('news.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
