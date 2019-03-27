from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<username>', views.userprofile, name='userprofile'),
    path('user/edit/', views.edit, name='editprofile'),
]