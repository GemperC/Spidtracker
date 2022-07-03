from this import d
from unittest.util import _MAX_LENGTH
from django import forms
from django.forms import ModelForm
from .models import Project, Issue


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("project_name", "pub_date", "owner", "description", "team", "tags")
        widgets = {
            "project_name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Project name'}),
            "pub_date": forms.DateInput(attrs={'class':'form-control'}),
            "owner": forms.Select(attrs={'class':'form-control', 'placeholder': 'Owner'}),
            "description": forms.Textarea(attrs={'class':'form-control', 'placeholder': '100 charecters limit', 'rows':5} ),
            "team": forms.Select(attrs={'class':'form-control', 'placeholder': 'Project Team'}),
            "tags": forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Tags'}),
        }


class ProjectURLForm(ModelForm):
    class Meta:
        model = Project
        fields = ("githubURL",)
        widgets = {
            "githubURL": forms.URLInput(attrs={'class':'form-control', 'placeholder': 'Github repository URL'}),
            }

class IssueForm(ModelForm):

    class Meta:
        model = Issue
        fields = ("issue_title", "description", "pud_date", "issue_creator", "bug_tags", "severity", 'project')
        widgets = {
            "issue_title": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Issue name'}),
            "description": forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            "pud_date": forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Created date'}),
            "issue_creator": forms.Select(attrs={'class':'form-control','placeholder': 'Issue submitter'}),
            "bug_tags": forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Issue Tags'}),
            "severity": forms.Select(attrs={'class':'form-control'}),
            "project": forms.Select(attrs={'class':'form-control'}),
        }

