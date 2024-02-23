from rest_framework import serializers
from .models import Queries


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields = '__all__'