from django import forms
from .models import Subject

class SelectSyllabusForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['faculty', 'year', 'part']