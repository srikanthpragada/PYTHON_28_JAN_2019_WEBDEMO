import requests
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

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
    return render(request,'ajax_demo.html')

def ajax_datetime(request):
    cd = datetime.now()
    return HttpResponse(str(cd))
