# Generated by Django 2.1.5 on 2019-03-13 22:50

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('image', pyuploadcare.dj.models.ImageField(blank=True, verbose_name='Tło')),
                ('body', models.TextField(verbose_name='Opis kategorii')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subscribers', models.ManyToManyField(blank=True, related_name='subscribed_boards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dział',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Embed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255)),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('description', tinymce.models.HTMLField(verbose_name='Opis')),
                ('thumbnail_url', models.URLField(max_length=255)),
                ('image', models.ImageField(upload_to='embedsimage')),
                ('html', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='embeds', to='boards.Board', verbose_name='Kategoria')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('body', tinymce.models.HTMLField(blank=True, verbose_name='Treść')),
                ('image', models.ImageField(blank=True, null=True, upload_to='subject')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='boards.Board', verbose_name='Kategoria')),
            ],
            options={
                'verbose_name': 'Post',
                'ordering': ['-created_at'],
            },
        ),
    ]
