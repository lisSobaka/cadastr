from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import QuerySerializer
from .models import Queries
from .services.filter_services import *


class QueryViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Queries.objects.all()
    model = Queries
    serializer_class = QuerySerializer


    def filter_queryset(self, queryset):
        queryset = queries_filtering(self,queryset)
        print(queryset)
        return queryset