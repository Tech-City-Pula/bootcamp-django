from django.urls import path
from moja_aplikacija.views import hello, greet_name, greet_person, rows

urlpatterns = [
    path('', hello),
    path('greet_name', greet_name),
    path('greet_name/<str:name>', greet_person),
    path('rows/<int:rows>', rows)
]