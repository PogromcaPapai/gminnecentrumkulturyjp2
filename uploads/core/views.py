from django.shortcuts import render
from core.models import Show, User, Reservation

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':

        return render(request, 'data_analysis.html',
                      {'result_present': True,
                       'results': {'r_table': r_table.to_html(),
                                   'p_table': p_table.to_html()},
                       'df': df.to_html()})

    return render(request, 'data_analysis.html')

def login_register(username, email, password):
    User.objects.get(username=username, password=password)
