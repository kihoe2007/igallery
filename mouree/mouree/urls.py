from django.urls import path
from django.views import gallery_view

urlpatterns = [
    path('', gallery_view, name='gallery'),
]