from django.shortcuts import render
import models

def home(request):
    return render(request, 'home.html')

def register(request):
    pass

def showlist(request):
    return render(request, 'event_list.html')

def reservation(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'reservation_page.html')
