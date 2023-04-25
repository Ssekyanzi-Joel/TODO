from django import forms
from .models import Task

class NewTask(forms.ModelForm):
    class Meta:
        model =Task
        fields = 'title','description','complete','due_date','priority','completed_date','tags'
        