from django.contrib import admin
from django.urls import path
from apps import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = 'landingpage'
urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)