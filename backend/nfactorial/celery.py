import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nfactorial.settings')

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

app = Celery('nfactorial', broker = CELERY_BROKER_URL, include = ['nfactorial.tasks'])
# app.conf.enable_utc = False

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(['nfactorial'])


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
