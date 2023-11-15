from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world. You're at myapp's view.")