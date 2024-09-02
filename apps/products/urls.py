from django.contrib import admin
from django.urls import path
from apps import *
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('<str:slug>/', ProductDetail.as_view(), name='product_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
