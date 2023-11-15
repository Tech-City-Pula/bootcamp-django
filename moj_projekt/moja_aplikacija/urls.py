from django.urls import path
from moja_aplikacija.views import hello, greet_name

urlpatterns = [
    path('', hello),
    path('greet_name', greet_name),
]