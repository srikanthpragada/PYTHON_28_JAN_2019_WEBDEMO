from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Title


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'title', 'author', 'price')


def rest_client(request):
    return render(request, 'rest_client.html')


@api_view(['GET', 'POST'])
def title_process(request):
    if request.method == "GET":
        books = Title.objects.all()
        serializer = TitleSerializer(books, many=True)
        # send all titles in the form of json
        return Response(serializer.data)
    else:  # POST, so insert a new row into table
        title = TitleSerializer(data=request.data)
        if title.is_valid():
            title.save()  # insert into table
            return Response(title.data)
        else:
            return Response(title.errors, status=400)  # bad request


@api_view(['GET', 'DELETE'])
def one_title_process(request, id):
    # check whether object is found
    try:
        book = Title.objects.get(id=id)
    except:
        return Response(status=404)  # Send 404 to client

    if request.method == "GET":
        # Convert Python object to Json and send to client
        serializer = TitleSerializer(book)
        return Response(serializer.data)
    else:  # Delete object from Table and send 204 as status code
        book.delete()
        return Response(status=204)  # No data
