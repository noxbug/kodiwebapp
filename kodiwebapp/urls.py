from django.urls import path

from . import views

app_name = 'kodiwebapp'

urlpatterns = [
    path('', views.index, name='index'),
    ### MENU ###
    path('translate_sub', views.translate_sub, name='translate_sub'),
    path('next_sub', views.next_sub, name='next_sub'),
    path('update', views.update, name='update'),
    ### PLAYER ###
    path('play/', views.play, name='play'),
    path('stop/', views.stop, name='stop'),
    path('fast_forward/', views.fast_forward, name='fast_forward'),
    path('fast_rewind/', views.fast_rewind, name='fast_rewind'),
    ### CONTROL ###
    path('control/', views.control, name='control'),
]