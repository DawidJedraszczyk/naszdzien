from django.contrib import admin
from django.urls import path
from apps import *
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)