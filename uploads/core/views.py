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
            f = User(username=processed['username'], password=processed['password'], email=processed['email'])
            f.save()
            return HttpResponseRedirect('/')
        else:
            new_form = Register()
            return render(request, 'registration_page.html', {'form':new_form})
    else:
        form = Register()
        return render(request, 'registration_page.html', {'form':form})

def showlist(request):
    events = Show.objects.all()
    return render(request, 'event_list.html')

def reservation(request):
    if request.method == 'POST':
        form = Reserve(request.POST)
        if form.is_valid():
            processed = form.cleaned_data
            accounts = User.objects(username=processed['username'], password=processed['password'])
            if len(accounts)==1:
                show_id = ''
                for i in request.path[1:]:
                    if i=='/':
                        break
                    else:
                        show_id += i
                show = Show(id_=int(show_id))

                seat = ''
                for i in request.path[-2::-1]:
                    if i=='/':
                        break
                    else:
                        seat = i + seat
                reserve_obj = Reservation(user = accounts, event = show, seat = seat)
                reserve_obj.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
    else:
        form = Reserve()
        return render(request, 'reservation_page.html', {'form':form})
