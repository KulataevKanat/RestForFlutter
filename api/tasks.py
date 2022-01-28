import datetime

from django.utils import timezone

from RestForFlutter.celery import app
from api.models import Announcement


@app.task
def deleting_data_over_time():
    ads = Announcement.objects.all()

    for ad in ads:
        expiration_date = ad.created + datetime.timedelta(seconds=1)
        if expiration_date < timezone.now():
            for image_instance in ad.image.all():
                image_instance.image.delete()
                image_instance.delete()
            ad.delete()


deleting_data_over_time()
