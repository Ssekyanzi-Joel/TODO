from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordsChangeView, New_Task,  TaskDetail, TaskUpdate, TaskDeleteView
# from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage, TaskReorder
# New_Task
urlpatterns = [
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', views.signout, name='logout'),


    path('', views.alltask_home, name='home'),
    path('confirmed_delete', views.success_OnDelete, name='confirm_deletion'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_details'),
    path('create-task/', New_Task.as_view(), name='create-task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='update_task'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('complete_task/', views.complete_task, name='complete_task'),
    # path('create-task/', views.create_task, name='create_task'),
    # path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

    # change password
    path('change-password/', PasswordsChangeView.as_view(
        template_name='passcode_reset/change-password.html'), name='change-password'),
    # forgot password / resetting security key
    # 1
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='passcode_reset/email_input_reset_password.html'),
         name='reset_password'),
    # 2
    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='passcode_reset/password_reset_sent.html'),
         name='password_reset_done'),
    # 3
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='passcode_reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # 4
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='passcode_reset/password_reset_complete.html'),
         name='password_reset_complete'),

]
