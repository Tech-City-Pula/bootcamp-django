from django.urls import path
from moja_aplikacija.views import hello, greet_name, greet_person

urlpatterns = [
    path('', hello),
    path('greet_name', greet_name),
    path('greet_person/<str:name>', greet_person),
]