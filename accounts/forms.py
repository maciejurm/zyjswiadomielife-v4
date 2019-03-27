from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from pyuploadcare.dj.forms import FileWidget, ImageField

class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileEditForm(ModelForm):
    photo = ImageField(widget=FileWidget(attrs={
        'data-image-shrink': '1024x1024',
        'data-tabs': 'file url facebook instagram',
        'data-preview-step': 'true',
        'data-crop' : 'free 16:9 4:3 5:4 1:1'
    }))

    class Meta:
        model = Profile
        fields = ['photo', 'bio', 'facebook', 'www']