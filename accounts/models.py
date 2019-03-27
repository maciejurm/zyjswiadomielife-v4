from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from autoslug import AutoSlugField
from pyuploadcare.dj.models import ImageField

NW = 'NW'
MAN = 'MN'
WOMAN = 'WM'
GENDER = (
    (MAN, 'Nie wybrano'),
    (MAN, 'Mężczyzna'),
    (WOMAN, 'Kobieta'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = ImageField(blank=True, manual_crop="" ,verbose_name='Awatar')
    image = models.ImageField(blank=True, null=True, verbose_name='Zdjęcie profilowe')
    gender = models.CharField(max_length=2, choices=GENDER, default=NW, verbose_name='Płeć')
    bio = models.TextField(blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    facebook = models.URLField(blank=True)
    www = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()