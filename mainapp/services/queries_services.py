import requests
import time
import random


# Функция принимает request и возвращает параметы запроса из URI
def get_params(request):
    params = request.build_absolute_uri().split('/')[-1]
    return params


# Функция-обработчик запроса. Делает запрос на внешний сервер, 
# передавая кадастровый номер, широту и долгоу, получает ответ (True/False)
def query_handler(request):
    # Получаем параметры запроса из URI
    params = get_params(request)
    if 'cadastr' not in params or 'latitude' not in params or 'longitude' not in params:
        return {'error': 'incorrect query'}, 400

    # Делаем запрос на внешний сервер, получаем от него результат (True/False)
    result = requests.get(f'http://127.0.0.1:8000/result/{params}').json()['result']

    query = request.GET
    save_query(query, result)
    return {'result': result}, 200


# Функция сохранения запроса и ответа сервера по API. 
def save_query(query, result):
    # Формируем словарь data, содержащий кадастровый номер, широту, 
    # долготу и ответ сервера
    data = {
        'cadastr': query['cadastr'],
        'latitude': query['latitude'],
        'longitude': query['longitude'],
        'result': result,

    }
    # Делаем POST запрос по API для сохранения запроса
    requests.post('http://127.0.0.1:8000/api/queries/', data=data)


# Имитация работы внешнего сервера. 
def get_result(request):
    # Получаем параметы запроса для последующей обработки
    query = {
        'cadastr': request.GET.get('cadastr'),
        'latitude': request.GET.get('latitude'),
        'longitude': request.GET.get('longitude')
    }

    # Случайно генерируем ответ сервера (True/False) и устанавливаем 
    # задержку обработки запроса (до 60 сек.)
    result = random.choice([True, False])
    delay = random.randint(0,3)
    time.sleep(delay)
    return {'result': result}, 200


# Проверка запуска сервера. Имитирует безотказный сервер, возвращает код 200
def ping_server():
    status = 200
    return {'status': status}, 200

# Функция возвращает историю всех запросов, либо запросов по конкретному 
# кадастровому номеру, если в запросе передан параметр cadastr
def get_history(request):
    params = get_params(request)
    print('!!!!', params)
    history = requests.get(f'http://127.0.0.1:8000/api/queries{params}').json()
    if len(history) == 0:
        return {'history': 'records are not found'}, 200
    return {'history': history}, 200