from django.forms import ModelForm
from .models import Subjectcomment, Embedcomment

class SubjectcommentForm(ModelForm):

    class Meta:
        model = Subjectcomment
        fields = ['body']

class EmbedcommentForm(ModelForm):

    class Meta:
        model = Embedcomment
        fields = ['body']