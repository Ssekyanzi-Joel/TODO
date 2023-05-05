from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Task
# forms
from .forms import NewTask, TagForm


class New_Task(CreateView):
    model = Task
    form_class = NewTask
    template_name = "task/task_form.html"

    def form_valid(self, NewTask):
        NewTask.instance.user = self.request.user
        return super().form_valid(NewTask)


class PasswordsChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

    success_message = "Password successfully changed...!"
    login_url = 'login'


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        this_user = authenticate(username=username, password=password)

        if this_user is not None:
            login(request, this_user)
            messages.success(request, 'Logged In')
            return redirect('home')

        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return '/'

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def signout(request):
    logout(request)
    messages.info(request, 'Logged Out..!')
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email_address']
        password = request.POST['password']

        myUser = User.objects.create_user(
            username, email, password)

        myUser.is_active = True

        myUser.save()

        messages.success(request, "Personal account created Successfully...!")

        return redirect("login")

    context = {
        messages: 'messages'
    }
    return render(request, 'accounts/register.html')


@login_required(login_url='login')
def alltask_home(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
    }
    return render(request, "task/task_list.html", context)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/task_details.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('home')


def success_OnDelete(request):
    return render(request, 'task/confirmed_delete.html')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    # context_object_name = 'task'm
    success_url = reverse_lazy('confirm_deletion')

    template_name = 'task/confirm_delete_task.html'


class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))
