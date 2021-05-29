from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    topic_description = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your topic here'}))
    snip_description = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your text here'}))

    class Meta:
        model = Snippet
        fields = [
        'topic_description', 'snip_description', 
        ]
