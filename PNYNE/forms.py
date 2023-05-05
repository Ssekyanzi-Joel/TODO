from django import forms
from django.forms import DateInput
from .models import Task, Tag


class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = 'title', 'description', 'complete', 'due_date', 'priority', 'completed_date', 'tags'
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'}),
        }
        tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
