from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['vote_total', 'vote_ratio']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'tags': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'title': 'Project Name',
            'description': 'Project Description',
            'tags': 'Project Tags',
        }
