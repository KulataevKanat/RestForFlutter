import datetime

from django.utils import timezone

from RestForFlutter.celery import app
from api.models import Publicity


@app.task
def deleting_data_over_time():
    publicity = Publicity.objects.all()

    for ad in publicity:
        expiration_date = ad.created + datetime.timedelta(minutes=1)
        if expiration_date < timezone.now():
            ad.delete()
