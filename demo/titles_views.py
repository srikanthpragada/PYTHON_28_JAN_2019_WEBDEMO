from django.db.models import Avg, Count
from django.shortcuts import render, redirect

from .forms import AddTitleForm
from .models import Title


def titles_home(request):
    summary = Title.objects.all(). \
        aggregate(count=Count('id'), avgprice=Avg('price'))
    return render(request, 'titles_home.html', {'summary': summary})


def titles_add(request):
    if request.method == "GET":
        f = AddTitleForm()
        return render(request, 'titles_add.html', {'form': f})
    else:
        f = AddTitleForm(request.POST)
        if f.is_valid():
            f.save()  # insert row into table
            return redirect("/demo/titles/list")

    return render(request, 'titles_add.html', {'form': f})


def titles_list(request):
    titles = Title.objects.all()
    return render(request, 'titles_list.html', {'titles': titles})


# /demo/titles/delete/<int:id>
def titles_delete(request, id):
    title = Title.objects.get(id=id)
    title.delete()  # Delete row from table
    return redirect("/demo/titles/list")


def titles_edit(request, id):
    message = ""
    if request.method == "GET":
        try:
            title = Title.objects.get(id=id)
            f = AddTitleForm(instance=title)
        except:
            return render(request, "titles_error.html",
                          {'message': f'Title Id [{id}] Not Found!'})
    else:
        # post
        title = Title.objects.get(id=id)
        f = AddTitleForm(instance=title, data=request.POST)
        try:
            f.save()
            message = "Title has been updated successfully!"
        except:
            message = "Sorry! Could not update title!"

    # Common for GET and POST
    return render(request, 'titles_edit.html',
                  {'message': message, 'form': f})

