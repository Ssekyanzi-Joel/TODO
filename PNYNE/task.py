from celery import shared_task
from django.core.mail import send_mail
from .models import Task
import datetime


@shared_task
def send_alert_emails():
    now = datetime.datetime.utcnow()
    upcoming_events = Task.objects.filter(
        date__lte=now + datetime.timedelta(days=1))

    for event in upcoming_events:
        send_mail(
            'Event Reminder',
            'The event "{}" is happening tomorrow.'.format(event.name),
            'todoassignment50@gmail.com',
            [Task.user.email],
        )
