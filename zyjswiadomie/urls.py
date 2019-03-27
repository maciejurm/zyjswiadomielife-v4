"""zyjswiadomie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from home.views import HomeList
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from boards.sitemaps import SubjectSitemap, EmbedSitemap

sitemaps = {
    'subjects': SubjectSitemap,
    'embeds': EmbedSitemap
}

urlpatterns = [
    path('', HomeList.as_view(), name='home'),
    path('jak-to-dziala/', TemplateView.as_view(template_name="jaktodziala.html"), name='jaktodziala'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('api/', include('likedislike.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    re_path(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^avatar/', include('initial_avatars.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
