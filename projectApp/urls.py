from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
path('registration/',views.register),
path('profile/',views.profile),
]