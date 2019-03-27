from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.BoardsPageView.as_view(), name='boardlist'),
    path('board/<slug>/', views.boarddetail, name='board'),
    path('list/', views.subjectlist, name='subject_list'),
    path('subject/<slug>/', views.subjectdetail, name='subject_detail'),
    re_path(r'^b/(?P<board>[-\w]+)/subscription/$', views.subscribe, name='subscribe'),
    path('addboard/', views.BoardCreate.as_view(), name='boardadd'),
    path('addsubject/', views.SubjectCreate.as_view(), name='subjectadd'),
    path('embed/<slug>', views.embeddetail, name='embeddetail'),
    path('embed/<int:pk>/edit/', views.EmbedUpdate.as_view(), name='embededit'),
    path('addembed/', views.save_embed, name='addembed'),
    re_path(r'^u/(?P<username>[\w.@+-]+)/subscriptions/$', views.UserSubscriptionListView.as_view(), name='user_subscription_list'),
    path('feed/', views.feed, name='feed'),
]
