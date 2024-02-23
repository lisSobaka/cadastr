FROM python:3.11-slim

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
