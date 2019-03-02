from django.http import HttpResponse
from datetime import datetime


# View to handle /welcome
def welcome(request):
    return HttpResponse("<h1>Welcome To Django</h1>")


# View to handle /wish
def wish(request):
    if 'name' in request.GET:
        name = request.GET["name"]
    else:
        name = "Unknown"

    hour = datetime.now().hour

    if hour < 12:
        msg = "Good Morning"
    elif hour < 16:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>Hello {name}, {msg}</h1>")
