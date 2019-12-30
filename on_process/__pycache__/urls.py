from django.urls import path

from . import views

urlpatterns = [
    path('', views.on_process, name='on_process'),
]
