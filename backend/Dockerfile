FROM python:3.10-slim

# Install locales and necessary packages
RUN apt-get update && \
    apt-get install -y locales locales-all && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /backend

COPY . /backend/
RUN pip install -r requirements.txt

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --no-input \
    && gunicorn nfactorial.wsgi:application --bind 0.0.0.0:8000 --log-level info
