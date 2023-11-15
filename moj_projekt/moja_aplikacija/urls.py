from django.urls import path
from moja_aplikacija.views import hello, greet_name, greet_person, rows, set_session, greet_name_from_session, submit_name

urlpatterns = [
    path('', hello),
    path('greet_name', greet_name),
    path('greet_name/<str:name>', greet_person),
    path('rows/<int:rows>', rows),
    path('set_session', set_session, name='set_session'),
    path('greet_name_from_session', greet_name_from_session),
    path('submit_name', submit_name),
]