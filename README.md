# Проект Cadastr
 Проект - тестовое задание.


Сервис принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, получает результат (True/False) и сохранеие данные запроса и ответ в локальную БД.

## Запуск:
> *Предполагается, что перед запуском проекта у пользователя уже установлен Docker*
1. Скопировать репозиторий на локальный компьютер, выполнив команду:
> git clone https://github.com/lisSobaka/cadastr/
2. Перейти в директорию проекта, выполнив команду:
> cd cadastr
3. Собрать образ, выполнив команду:
> docker build -t cadastr .
4. Запустить образ, выполнив команду:
> docker run -p 8000:8000 cadastr

Проект будет развёрнут по адресу http://127.0.0.1:8000/

## Эндпоинты: 
### /query

Обработчик запросов

Принимает GET запрос с параметрами в формате:

> /query?cadastr={Кадастровый номер}&latitude={Широта}&longitude={Долгота}

Возвращает словарь с результатом ответа внешнего сервера в формате:

> {"result": True/False}

### /ping

Принимает GET запрос без указания параметров

Возвращает словарь в формате:

> {"status": 200}

### /history

Принимает GET запрос с указанием кадастрового номера в формате:

> http://127.0.0.1:8000/history?cadastr={Кадастровый номер}

Возвращает словарь со списком всех запросов по кадастровому номеру в формате:

> {"history": [{query_1},{query_1}]}

Либо, если записи в базу не обнаружены, словарь:

> {"history": "records are not found"}

Если в GET запросе не были переданы параметры, возвращает словарь со списком всех запросов, имеющихся в БД в формате: 

> {"history": [{query_1},{query_1}]}

## Админ-панель

У сервиса реализована админ-панель, позволяющая просматривать все записи в БД, а так же создавать новые. Доступна по адресу:

> http://127.0.0.1:8000/admin

Данные суперпользователя:

login: admin <br>
password: 1234

## Примеры работы сервиса:

Создание нового запроса:

> http://127.0.0.1:8000/query/?cadastr=47:14:423201:777&longitude=E32.612323&latitude=N52.722361

Поиск запроса в БД:

> http://127.0.0.1:8000/history?cadastr=47:14:423201:777

Получение всех запросов из БД

> http://127.0.0.1:8000/history

Проверка готовности внешнего сервера:

> http://127.0.0.1:8000/ping