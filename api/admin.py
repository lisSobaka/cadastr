from django.contrib import admin
from .models import Queries

@admin.register(Queries)
class QueriesAdmin(admin.ModelAdmin):
    list_display = ('cadastr', 'longitude', 'latitude', 'result', 'date')
    ordering = ('-date',)
    list_filter = ('date',)

