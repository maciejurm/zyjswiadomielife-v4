from django.contrib.sitemaps import Sitemap
from .models import Subject, Embed
 
 
class SubjectSitemap(Sitemap):    
    priority = 0.9
 
    def items(self):
        return Subject.objects.all()
 
class EmbedSitemap(Sitemap):
    priority = 0.9

    def items(self):
        return Embed.objects.all()