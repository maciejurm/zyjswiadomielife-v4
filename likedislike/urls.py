from django.urls import re_path
from django.contrib.auth.decorators import login_required
     
from . import views
from .models import LikeDislike
from boards.models import Subject, Embed
     
app_name = 'ajax'
urlpatterns = [
    re_path(r'^subject/(?P<pk>\d+)/like/$',
            login_required(views.VotesView.as_view(model=Subject, vote_type=LikeDislike.LIKE)),
            name='subject_like'),
    re_path(r'^subject/(?P<pk>\d+)/dislike/$',
            login_required(views.VotesView.as_view(model=Subject, vote_type=LikeDislike.DISLIKE)),
            name='subject_dislike'),
    re_path(r'^embed/(?P<pk>\d+)/like/$',
            login_required(views.VotesView.as_view(model=Embed, vote_type=LikeDislike.LIKE)),
            name='embed_like'),
    re_path(r'^embed/(?P<pk>\d+)/dislike/$',
            login_required(views.VotesView.as_view(model=Embed, vote_type=LikeDislike.DISLIKE)),
            name='embed_dislike'),
]