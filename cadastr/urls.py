
from django.contrib import admin
from django.urls import path, include
from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('api/', include('api.urls')),
]
