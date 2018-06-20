from django.shortcuts import render, redirect
from django.http import HttpResponse

import lib.kodirpc as kodi

# Connect to kodi
kodi.connection.connect('192.168.1.10')

# Create your views here.


def index(request):
    kodi.nowplaying.update()
    context = {'kodi': kodi}
    return render(request, 'kodiwebapp/now_playing.html', context)


### MENU ###
def translate_sub(request):
    return HttpResponse('translate sub page')


def next_sub(request):
    return HttpResponse('next sub page')


def update(request):
    return HttpResponse('update library page')


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