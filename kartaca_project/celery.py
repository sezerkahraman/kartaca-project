import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kartaca_project.settings")

app = Celery("kartaca_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()