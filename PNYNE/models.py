from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    # the field can be empty.
    due_date = models.DateTimeField(null=True, blank=True)
    # the field can be empty.
    priority = models.CharField(max_length=20, null=True, blank=True)
    # the field can be empty.
    completed_date = models.DateTimeField(null=True, blank=True)
    # tasks can be associated with multiple tags
    tags = models.OneToOneField('Tag', blank=True)

    # human readable string representation of task
    def __str__(self):
        return self.title

    class Meta:
        # tasks should be ordered based on their associsted user
        order_with_respect_to = 'user'

    def mark_as_complete(self):
        self.complete = True
        self.completed_date = timezone.now()
        self.save()

    def mark_as_incomplete(self):
        self.complete = False
        self.completed_date = None
        self.save()

    @staticmethod
    def get_all_completed_tasks():
        return Task.objects.filter(complete=True)

    @staticmethod
    def get_tasks_due_today():
        return Task.objects.filter(due_date=datetime.today())

    def get_absolute_url(self):
        return reverse("home")


class Tag(models.Model):  # Tag model that represents a tag that can be associated with tasks
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
