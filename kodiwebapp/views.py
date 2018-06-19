from django.shortcuts import render
from django.http import HttpResponse

import lib.kodirpc as kodi


kodi.connection.connect('192.168.1.10')

# Create your views here.

def index(request):
    #context = {'kodi': kodi}
    #return render(request, 'kodiwebapp/base/base.html')
    return HttpResponse('You are at the main site')


def play(request):
    return HttpResponse('play/pause')


def stop(request):
    return HttpResponse('Stopping NOW!')