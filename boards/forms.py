from django.forms import ModelForm
from .models import Board, Subject
from django import forms
from pyuploadcare.dj.forms import FileWidget, ImageField

class BoardForm(ModelForm):

    image = ImageField(widget=FileWidget(attrs={
        'data-image-shrink': '2024x2024',
        'data-tabs': 'file url',
        'data-preview-step': 'true',
        'data-crop' : 'free 16:9 4:3 5:4 1:1'
    }))

    class Meta:
        model = Board
        fields = ['title', 'image', 'body']


class Subject(ModelForm):
    
    class Meta:
        model = Subject
        fields = ['title', 'body', 'board']

class SubmitEmbed(forms.Form):
    url = forms.URLField()
    board = forms.ModelChoiceField(label="Kategoria", queryset=Board.objects.all().order_by('title'), required=False)

