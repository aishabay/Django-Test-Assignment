FROM python:3.10.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend

WORKDIR /app/backend

RUN python manage.py migrate

RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')" | python manage.py shell

COPY backend/media.zip /app/backend/
COPY backend/mydata.json /app/backend/

RUN apt-get update \
    && apt-get install -y unzip \
    && unzip media.zip -d media \
    && rm media.zip

RUN python manage.py loaddata mydata.json

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
