# Generated by Django 2.1.5 on 2019-03-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_remove_embed_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embed',
            name='thumbnail_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
