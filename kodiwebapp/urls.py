from django.urls import path

from . import views

app_name = 'kodiwebapp'

urlpatterns = [
    ### DEBUG ###
    path('base/', views.base, name='base'),
    path('player/', views.player_view, name='player'),
    path('player/<int:playlist_position>/', views.player_view, name='go_to_playlist_position'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('artists/', views.artist_view, name='artists'),
    path('albums/', views.album_view, name='albums'),
    path('albums/<int:artist_id>/', views.album_view, name='artist_albums'),
    path('songs/', views.song_view, name='songs'),
    path('songs/<int:album_id>/', views.song_view, name='album_songs'),
    ### INDEX ###
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
    path('up/', views.up, name='up'),
    path('down/', views.down, name='down'),
    path('left/', views.left, name='left'),
    path('right/', views.right, name='right'),
    path('select/', views.select, name='select'),
    path('back/', views.back, name='back'),
    path('home/', views.home, name='home'),
    path('context_menu/', views.context_menu, name='context_menu'),
    path('info/', views.info, name='info'),
    ### PLAYLIST ###
    path('playlist/', views.playlist, name='playlist'),
    path('playlist/<int:position>', views.playlist_select, name='playlist_select'),
]