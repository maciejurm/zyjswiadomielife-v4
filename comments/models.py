from django.db import models
from django.contrib.auth.models import User
from boards.models import Subject, Embed

class Comment(models.Model):
    body = models.TextField(verbose_name='Treść komentarza:')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

class Subjectcomment(Comment):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjectcomments')

    def __str__(self):
        return "Użytkownik {} skomentował post {}".format(self.author, self.subject)

class Embedcomment(Comment):
    embed = models.ForeignKey(Embed, on_delete=models.CASCADE, related_name='embedcomments')