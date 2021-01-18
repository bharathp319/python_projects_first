from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def welcome(request, date=None):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    m = 'Hello bharath very  '
    if h < 12:
        m += 'Good Moring'

    elif h < 15:
        m += 'Good Afternoon'

    elif h < 20:
        m += "Good Evening and the time is " + f"{date}"

    else:
        m += "Good Night"

    return HttpResponse(m)

def hello(request):
    return HttpResponse("hello from django")
