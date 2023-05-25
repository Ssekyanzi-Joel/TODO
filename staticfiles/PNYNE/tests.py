from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Task
from .forms import NewTask


class TaskTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')


def test_new_task_view(self):
    response = self.client.post(reverse('new_task'), {
        'title': 'Test Task',
        'description': 'This is a test task',
        'complete': False,
    })
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Task.objects.count(), 1)


def test_password_change_view(self):
    response = self.client.post(reverse('password_change'), {
        'old_password': 'testpass',
        'new_password1': 'newpass',
        'new_password2': 'newpass',
    })
    self.assertEqual(response.status_code, 302)
    self.assertEqual(get_messages(response.wsgi_request)[
                     0].message, 'Password successfully changed...!')


def test_signin_function(self):
    response = self.client.post(reverse('signin'), {
        'username': 'testuser',
        'password': 'testpass',
    })
    self.assertEqual(response.status_code, 302)
    self.assertEqual(get_messages(response.wsgi_request)
                     [0].message, 'Logged In')


def test_signout_function(self):
    response = self.client.get(reverse('signout'))
    self.assertEqual(response.status_code, 302)
    self.assertEqual(get_messages(response.wsgi_request)
                     [0].message, 'Logged Out..!')


def test_signup_function(self):
    response = self.client.post(reverse('signup'), {
        'username': 'newuser',
        'email_address': 'newuser@example.com',
        'password': 'newpass',
    })
    self.assertEqual(response.status_code, 302)
    self.assertEqual(get_messages(response.wsgi_request)[
                     0].message, 'Personal account created Successfully...!')


def test_alltask_home_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)


def test_task_create_view(self):
    response = self.client.post(reverse('new_task'), {
        'title': 'Test Task',
        'description': 'This is a test task',
        'complete': False,
    })
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Task.objects.count(), 1)


def test_task_update_view(self):
    task = Task.objects.create(
        user=self.user,
        title='Test Task',
        description='This is a test task',
        complete=False,
    )
    response = self.client.post(reverse('update_task', args=[task.id]), {
        'title': 'Updated Task',
        'description': 'This is an updated task',
        'complete': True,
    })
    self.assertEqual(response.status_code, 302)
    task.refresh_from_db()
    self.assertEqual(task.title, 'Updated Task')
    self.assertEqual(task.description, 'This is an updated task')
    self.assertEqual(task.complete, True)


def test_task_delete_view(self):
    task = Task.objects.create(
        user=self.user,
        title='Test Task',
        description='This is a test task',
        complete=False,
    )
    response = self.client.post(reverse('delete_task', args=[task.id]))
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Task.objects.count(), 0)
