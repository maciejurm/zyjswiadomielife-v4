# Generated by Django 2.1.5 on 2019-03-13 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='embed',
            name='image',
        ),
    ]
