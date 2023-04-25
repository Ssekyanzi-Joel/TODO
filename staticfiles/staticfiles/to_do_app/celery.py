
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta
from .task import send_due_date_reminders

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do_app.settings')

app = Celery('to_do_app')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



app.conf.beat_schedule = {
    'send_due_date_reminders': {
        'task': 'to_do_app.tasks.send_due_date_reminders',
        'schedule': timedelta(days=1),
    },
}
