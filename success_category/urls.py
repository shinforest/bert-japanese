from django.urls import path

from . import views

urlpatterns = [
    path('', views.success_category, name='success_category'),
]
