# tasks.py
from datetime import date, timedelta
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from .models import Task

@shared_task
def send_due_date_reminders():
    due_date = date.today() + timedelta(days=1)
    tasks_due_tomorrow = Task.objects.filter(due_date=due_date)

    for task in tasks_due_tomorrow:
        send_mail(
            subject=f'Reminder: Task "{task.title}" is due tomorrow',
            message=f'This is a reminder that your task "{task.title}" is due tomorrow.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[task.owner.email],
            fail_silently=False,
        )
