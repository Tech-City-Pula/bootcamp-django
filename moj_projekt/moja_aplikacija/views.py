from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, world. You're at myapp's view.")

def greet_name(request):
    context = {'name': 'Matej'}
    return render(request, 'greet_name.html', context)
