from django import forms
from .models import Note
from django.contrib.sessions.models import Session
from django.utils import timezone

class AddNote(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateTimeField(label='Date', widget=forms.TextInput(attrs={'class': 'input-group date form-control input-sm', 'data-provide':"datepicker"}))
    text = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control'}))
