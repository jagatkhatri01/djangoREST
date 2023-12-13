from django.urls import path
from home.views import ListUser, index, person

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('persons/', ListUser.as_view()),
]
