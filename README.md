# Django-Test-Assignment

## Installation to run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata mydata.json
unzip media.zip
python manage.py runserver
```
## Installation to run using docker

To build and start container:
```bash
docker-compose up -d --build
```

To stop and remove container:
```bash
docker-compose down
```

## Testing
Go to "http://127.0.0.1:8000/" on your browser and you will see the main page.
Go to "http://127.0.0.1:8000/admin", enter "admin" as username and "adminpassword" as password to access the admin page.
