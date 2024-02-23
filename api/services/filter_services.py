# Функция фильтрации. Проверяет, имеется ли в запросе параметр cadastr,
# если имеется - возвращает только запросы по указанному номеру
def queries_filtering(self, queryset):
    if 'cadastr' in self.request.GET:
        queryset = queryset.filter(cadastr=self.request.GET['cadastr'])
    return queryset