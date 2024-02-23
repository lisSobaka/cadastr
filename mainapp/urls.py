from django.urls import path
from .views import *

urlpatterns = [
    path('query/', query, name='query'),
    path('result/', return_result, name='return_result'),
    path('ping/', ping, name='ping_server'),
    path('history/', history, name='history'),
]
