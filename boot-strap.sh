sleep 15
./manage.py makemigrations
./manage.py migrate
#gunicorn --bind 0.0.0.0:8007 kartaca_project.wsgi --daemon
celery -A kartaca_project beat -l info --detach
celery -A kartaca_project worker -l info --detach
./manage.py runserver 0.0.0.0:8007 --noreload
exec "$@"