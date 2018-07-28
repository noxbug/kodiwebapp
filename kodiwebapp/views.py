from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from kodiwebapp.lib.subtitle.subtitle import Subtitle
from kodiwebapp.lib.widgets.widgets import Widgets
from time import sleep
import kodiwebapp.lib.kodirpc as kodi


# Connect to kodi
kodi.connection.connect('192.168.1.10')

# Initialize widgets
widgets = Widgets()
widgets.title = 'Now playing'
widgets.branding = 'Kodi web app'
widgets.app_bar_buttons = [
    {'label': 'NEW'},
    {'label': 'EDIT'},
    ]
widgets.menu = [
    {'label': 'Update library', 'url': 'kodiwebapp:update'},
    ]
widgets.navigation_drawer = [
    {'label': 'Now Playing', 'url': reverse_lazy('kodiwebapp:player')},
    {'label': 'Playlist', 'url': reverse_lazy('kodiwebapp:playlist')},
    {'label': 'Artists', 'url': reverse_lazy('kodiwebapp:artists')},
    {'label': 'Albums', 'url': reverse_lazy('kodiwebapp:albums')},
    {'label': 'Songs', 'url': reverse_lazy('kodiwebapp:songs')},
    ]
widgets.list_view = []

# Create your views here.

def base(request):
    context = {'widgets': widgets}
    return render(request, 'kodiwebapp/base.html', context)


def player_view(request, playlist_position=None):
    # copy widgets
    mywidgets = widgets.copy()
    mywidgets.title = 'Now playing'
    mywidgets.list_view = []
    # actions
    if playlist_position:
        kodi.player.go_to_playlist_position(playlist_position)
    else:
        kodi.nowplaying.update()
    # return
    context = {'kodi': kodi, 'widgets': mywidgets}
    return render(request, 'kodiwebapp/player.html', context)


def playlist_view(request):
    # copy widgets
    mywidgets = widgets.copy()
    mywidgets.title = 'Playlist'
    # get items
    playlist = kodi.playlist.get_items()
    # parse playlist items
    for i,item in enumerate(playlist):
        item['detail'] = item['artist'][0] + ' | ' + item['album']
        item['url'] = reverse_lazy('kodiwebapp:player') + str(i) + '/'
    mywidgets.list_view = playlist
    # return
    context = {'widgets': mywidgets}
    return render(request, 'kodiwebapp/base.html', context)


def artist_view(request):
    # copy widgets
    mywidgets = widgets.copy()
    mywidgets.title = 'Artists'
    # get artists
    artists = kodi.audiolibrary.get_artists()
    # parse artists
    for artist in artists:
        artist['url'] = reverse_lazy('kodiwebapp:albums') + str(artist['artistid']) + '/'
    mywidgets.list_view = artists
    # return
    context = {'widgets': mywidgets}
    return render(request, 'kodiwebapp/base.html', context)


def album_view(request, artist_id=None):
    # copy widgets
    mywidgets = widgets.copy()
    mywidgets.title = 'Albums'
    # get albums
    if artist_id:
        albums = kodi.audiolibrary.get_albums(artistid=artist_id)
    else:
        albums = kodi.audiolibrary.get_albums()
    for album in albums:
        album['url'] = reverse_lazy('kodiwebapp:songs') + str(album['albumid']) + '/'
    mywidgets.list_view = albums
    # return
    context = {'widgets': mywidgets}
    return render(request, 'kodiwebapp/base.html', context)


def song_view(request, album_id=None):
    # copy widgets
    mywidgets = widgets.copy()
    mywidgets.title = 'Songs'
    # get albums
    if album_id:
        artists = kodi.audiolibrary.get_songs(albumid=album_id)
    else:
        artists = kodi.audiolibrary.get_songs()
    mywidgets.list_view = artists
    # return
    context = {'widgets': mywidgets}
    return render(request, 'kodiwebapp/base.html', context)

### INDEX ###
def index(request):
    kodi.nowplaying.update()
    context = {'kodi': kodi, 'widgets': widgets}
    return render(request, 'kodiwebapp/base.html', context)


### MENU ###
def translate_sub(request):
    subtitle = Subtitle
    item = kodi.player.get_item()
    subtitle.translate(item['file'])
    # wait for kodi to discover the new file
    sleep(3)
    # jump to next subtitle file
    kodi.player.next_subtitle()
    return redirect('kodiwebapp:index')


def next_sub(request):
    kodi.player.next_subtitle()
    return redirect('kodiwebapp:index')


def update(request):
    kodi.library.update()
    return redirect('kodiwebapp:index')


### PLAYER ###
def play(request):
    kodi.player.play_pause()
    return redirect('kodiwebapp:index')


def stop(request):
    kodi.player.stop()
    return redirect('kodiwebapp:index')


def fast_forward(request):
    kodi.player.fast_forward()
    return redirect('kodiwebapp:index')


def fast_rewind(request):
    kodi.player.fast_rewind()
    return redirect('kodiwebapp:index')


### CONTROL ###
def control(request):
    context = {'kodi': kodi}
    return render(request, 'kodiwebapp/control.html', context)


def up(request):
    kodi.input.up()
    return redirect('kodiwebapp:control')


def down(request):
    kodi.input.down()
    return redirect('kodiwebapp:control')


def left(request):
    kodi.input.left()
    return redirect('kodiwebapp:control')


def right(request):
    kodi.input.right()
    return redirect('kodiwebapp:control')


def select(request):
    kodi.input.select()
    return redirect('kodiwebapp:control')


def back(request):
    kodi.input.back()
    return redirect('kodiwebapp:control')


def home(request):
    kodi.input.home()
    return redirect('kodiwebapp:control')


def context_menu(request):
    kodi.input.context_menu()
    return redirect('kodiwebapp:control')


def info(request):
    kodi.input.info()
    return redirect('kodiwebapp:control')


### PLAYLIST ###
def playlist(request):
    items = kodi.playlist.get_items()
    context = {'kodi': kodi, 'playlist': items}
    return render(request, 'kodiwebapp/playlist.html', context)


def playlist_select(request, position):
    kodi.player.go_to_playlist_position(position)
    return redirect('kodiwebapp:index')

