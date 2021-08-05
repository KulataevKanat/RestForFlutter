import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RestForFlutter.settings')

app = Celery('RestForFlutter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-data-every-year': {
        'task': 'api.tasks.deleting_data_over_time',
        'schedule': crontab(minute='*/1'),
    },

}
