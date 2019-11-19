from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import User, Show, Reservation
from .forms import Reserve, Register


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            processed = form.cleared_data
            f = User(username=processed['username'],
                     password=processed['password'], email=processed['email'])
            f.save()
            return HttpResponseRedirect('/')
        else:
            new_form = Register()
            return render(request, 'registration_page.html', {'form': new_form})
    else:
        form = Register()
        return render(request, 'registration_page.html', {'form': form})


def showlist(request):
    events = Show.objects.all()
    return render(request, 'event_list.html', {'events':events})

def showdetails(request, show_id):
    show = Show.objects(id_=int(show_id))
    if len(show)==1:
        reserved = Reservation.objects(event=show)
        room = [[False for i in range(10)] for j in range(10)]
        for i in reserved:
            room[i['row']][i['column']] = True
        return render(request, 'show.html', {'room': room, 'title': show['name'], 'desc': show['description'], 'date': show['date'], 'hour': show['hour']})
    else:
        return HttpResponseRedirect('/')

def reservation(request, show_id, seat):
    if request.method == 'POST':
        form = Reserve(request.POST)
        if form.is_valid():
            processed = form.cleaned_data
            accounts = User.objects(
                username=processed['username'], password=processed['password'])
            if len(accounts) == 1:
                show = Show.objects(id_=int(show_id))
                reserve_obj = Reservation(user=accounts, event=show, seat=seat)
                reserve_obj.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
    else:
        form = Reserve()
        return render(request, 'reservation_page.html', {'form': form})