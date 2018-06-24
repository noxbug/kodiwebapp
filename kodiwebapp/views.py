from django.shortcuts import render, redirect
from django.http import HttpResponse
from kodiwebapp.lib.subtitle.subtitle import Subtitle
from kodiwebapp.lib.widgets.widgets import Widgets
from time import sleep
import kodiwebapp.lib.kodirpc as kodi


# Connect to kodi
kodi.connection.connect('192.168.1.10')


# Initialize widgets
widgets = Widgets()
widgets.app = {'name': 'Now playing', 'branding': 'Kodi web app'}
widgets.app_bar_buttons = [
    {'label': 'NEW'},
    {'label': 'EDIT'},
    {'label': 'menu', 'icon': 'more_vert'},
    ]
widgets.navigation_drawer = [
    {'label': 'Music', 'url': '#'},
    {'label': 'Videos', 'url': '#'},
    {'label': 'TV Shows', 'url': '#'},
    {'label': 'Settings', 'url': '#'},
    ]
widgets.list_view = [
    {'label': 'This is the subject of my messige','detail': 'The body of the messige comes here. Beware that it can be verry long but the template should handle it fine. At least normally'},
    {'label': 'Item 2'},
    {'label': 'Item 3'},
    {'label': 'Item 4'},
    {'label': 'Item 1'},
    {'label': 'Item 2'},
    {'label': 'END-1'},
    {'label': 'END'},
    ]

# Create your views here.

### DEBUG VIEWS ###
def base(request):
    context = {'widgets': widgets}
    return render(request, 'kodiwebapp/base.html', context)


def base_nav(request):
    return render(request, 'kodiwebapp/base_nav.html')


def base_nav_ui(request):
    return render(request, 'kodiwebapp/base_nav_ui.html')


def base_nav_ui_content(request):
    return render(request, 'kodiwebapp/base_nav_ui.html')

### INDEX ###
def index(request):
    kodi.nowplaying.update()
    context = {'kodi': kodi}
    return render(request, 'kodiwebapp/now_playing.html', context)


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

