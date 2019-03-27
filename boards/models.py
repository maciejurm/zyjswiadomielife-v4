from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from autoslug import AutoSlugField
from django.urls import reverse
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from likedislike.models import LikeDislike
from pyuploadcare.dj.models import ImageField
from tinymce import HTMLField
from django_random_queryset import RandomManager

class Board(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    slug = AutoSlugField(populate_from='title', unique=True)
    image = ImageField(blank=True, manual_crop="" ,verbose_name='Tło')
    body = models.TextField(verbose_name='Opis kategorii')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name='subscribed_boards', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = RandomManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name='Dział'

    def get_absolute_url(self):
        return reverse('board',
                        args=[self.slug])



class Subject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    slug = AutoSlugField(populate_from='title', unique=True)
    body = HTMLField(blank=True, verbose_name='Treść')
    image = models.ImageField(upload_to='subject', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='subjects', verbose_name='Kategoria')
    votes = GenericRelation(LikeDislike, related_query_name='subjectsvotes')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'

    def get_absolute_url(self):
        return reverse('subject_detail',
                       args=[self.slug])

class Embed(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    description = HTMLField(verbose_name='Opis')
    thumbnail_url = models.URLField(max_length=255, blank=True, null=True)
    html = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, blank=True, null=True, related_name='embeds', verbose_name='Kategoria')
    votes = GenericRelation(LikeDislike, related_query_name='embedvotes')
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('embeddetail',
                       args=[self.slug])

    class Meta:
        ordering = ['-created_at']