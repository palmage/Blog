FROM python:3.9.1

WORKDIR /code
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .

CMD gunicorn blog.wsgi:application --bind 0.0.0.0:8000
