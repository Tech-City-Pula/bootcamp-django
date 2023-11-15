from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, world. You're at myapp's view.")

def greet_name(request):
    context = {'name': 'Matej'}
    return render(request, 'greet_name.html', context)

def greet_person(request, name):
    context = {'name': name.capitalize()}
    return render(request, 'greet_name.html', context)

def rows(request, rows):
    rows = range(rows)
    context = {'rows': rows}
    return render(request, 'rows.html', context)