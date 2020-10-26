


from django.shortcuts import render
from.utils import *

# Create your views here.

def index(request):
    today_rest_time = rest_of_day()
    context = {'today_rest_time': today_rest_time['today_rest_time']}
    return render(request, 'frontend/index.html', context)