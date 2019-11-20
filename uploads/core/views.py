from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import User, Show, Reservation
from .forms import Reserve, Register, NewShow


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

###

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            processed = form.cleaned_data
            accounts = User.objects.filter(username=processed['username'])
            if len(accounts)!=0:
                return render(request, 'error.html', {'error':"Istnieje już konto o takim loginie"})
            f = User(username=processed['username'],
                     password=processed['password'], email=processed['email'])
            f.save()
            return render(request, 'done.html')
        else:
            return render(request, 'error.html', {'error':form.errors})
    else:
        form = Register()
        return render(request, 'registration_page.html', {'form': form})


def showlist(request):
    events = Show.objects.all()
    return render(request, 'event_list.html', {'events':events})

def showdetails(request, show):
    shows = Show.objects.filter(id=int(show))
    if len(shows)==1:
        show = shows[0]
        reserved = Reservation.objects.filter(event=show)
        room = [[False for i in range(10)] for j in range(10)]
        for i in reserved:
            room[i.column][i.row] = True
        return render(request, 'show.html', {'room': room, 'range':range(10), 'show': show})
    else:
        return render(request, 'error.html', {'error':"Takie wydarzenie nie istnieje"})

def reservation(request, show, column, row):
    if request.method == 'POST':
        reserved = Reservation.objects.filter(event=show, column=column, row=row)
        if len(reserved)!=0:
            return render(request, 'error.html', {'error':"To miejsce jest już zarezerwowane"})
        form = Reserve(request.POST)
        if form.is_valid():
            processed = form.cleaned_data
            accounts = User.objects.filter(
                username=processed['username'], password=processed['password'])
            if len(accounts) == 1:
                show = Show.objects.filter(id=int(show))[0]
                reserve_obj = Reservation(user=accounts[0], event=show, column = column, row = row)
                reserve_obj.save()
                return render(request, 'done.html')
            else:
                return render(request, 'error.html', {'error':"Niepoprawne dane logowania"})
        else:
            return render(request, 'error.html', {'error':form.errors})
    else:
        reserved = Reservation.objects.filter(event=show, column=column, row=row)
        if len(reserved)!=0:
            return render(request, 'error.html', {'error':"To miejsce jest już zarezerwowane"})
        form = Reserve()
        return render(request, 'reservation_page.html', {'form': form})

def showform(request):
    if request.method == 'POST':
        form = NewShow(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'done.html')
        else:
            return render(request, 'error.html', {'error':form.errors})
    else:
        form = NewShow()
        return render(request, 'newshow.html', {'form':form})