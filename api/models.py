from django.db import models
from django.utils import timezone


class Queries(models.Model):
    class Meta:
        verbose_name_plural = 'Запросы'

    cadastr = models.CharField(max_length=20, 
                               verbose_name='Кадастровый номер')
    longitude = models.CharField(max_length=10, 
                               verbose_name='Долгота')
    latitude = models.CharField(max_length=10, 
                               verbose_name='Широта')
    result = models.BooleanField(verbose_name='Ответ сервера')
    date = models.DateTimeField(default=timezone.now,
                                verbose_name='Дата запроса')
    
    def __str__(self) -> str:
        return self.cadastr