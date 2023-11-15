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

def set_session(request):
    name = request.GET.get('name', 'Default Name')  # Replace 'Default Name' with a default value
    request.session['name'] = name
    return HttpResponse('Session set')

def greet_name_from_session(request):
    return render(request, 'greet_name_from_session.html')

def submit_name(request):
    return render(request, 'submit_name.html')