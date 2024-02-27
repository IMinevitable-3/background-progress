## Real time progress of celery task using django channels

` celery -A server  worker -l info`

### Set up

```
git clone https://github.com/IMinevitable-3/background-progress.git &&

cd background-progress &&
virtualenv env &&
source env/bin/activate &&
cd server   &&
pip install -r requirements.txt &&
python manage.py runserver
```

```
docker-compose build
docker-compose up

```
