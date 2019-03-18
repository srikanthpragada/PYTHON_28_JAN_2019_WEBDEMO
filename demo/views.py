from datetime import datetime

import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models import Course


# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome To Demo Application </h1>")


def show_course(request):
    c = Course("Data Science With Python", 36, 5000,
               ["Stats", "Pandas", "Matplotlib", "ML"])
    return render(request, 'course.html', {'course': c})


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    selcountries = filter(lambda c: c['region'] == 'Asia', countries)
    return render(request, 'countries.html',
                  {'countries': selcountries})


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def ajax_datetime(request):
    cd = datetime.now()
    return HttpResponse(str(cd))


def session_names(request):
    # either take existing names or empty list
    if 'names' in request.session:
        names = request.session['names']
    else:
        names = []

    if 'fullname' in request.GET:
        # add name to list
        fullname = request.GET["fullname"]
        names.append(fullname)
        request.session['names'] = names

    return render(request, 'sessions.html', {'names': names})
