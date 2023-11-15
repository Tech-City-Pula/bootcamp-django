from django.urls import path
from moja_aplikacija.views import hello

urlpatterns = [
    path('', hello, name='my_view'),
]