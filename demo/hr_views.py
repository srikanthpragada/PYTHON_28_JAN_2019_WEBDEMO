import sqlite3

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import AddJobForm


def add_job(request):
    if request.method == "GET":
        return render(request, 'add_job.html')
    else:  # Post
        # Process data and redirect to list of jobs
        title = request.POST['title']
        minsal = request.POST['minsal']
        try:
            con = sqlite3.connect(r"e:\classroom\python\hr.db")
            cur = con.cursor()
            cur.execute("insert into jobs(title,minsal) values(?,?)",
                        (title, minsal))
            con.commit()
            return HttpResponseRedirect("/demo/jobs/")
        except:
            return HttpResponse("<h3>Sorry! Could not add job due to some error! </h3")


def add_job_with_form(request):
    if request.method == "GET":
        f = AddJobForm()
        return render(request, 'add_job_form.html', {'form' : f})
    else:  # Post
        # Process data and redirect to list of jobs
        f = AddJobForm(request.POST)
        if f.is_valid():
          title = f.cleaned_data["title"]
          minsal =f.cleaned_data["minsal"]
          try:
            con = sqlite3.connect(r"e:\classroom\python\hr.db")
            cur = con.cursor()
            cur.execute("insert into jobs(title,minsal) values(?,?)",
                        (title, minsal))
            con.commit()
            return HttpResponseRedirect("/demo/jobs/")
          except:
            return HttpResponse("<h3>Sorry! Could not add job due to some error! </h3")
        else:
            # redisplay form with errors on invalid data
            return render(request, 'add_job_form.html', {'form': f})


def list_jobs(request):
    con = sqlite3.connect(r"e:\classroom\python\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs")
    jobs = cur.fetchall()
    return render(request, 'list_jobs.html', {'jobs': jobs})
