from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import reverse
from wiki.models import BattleCat


class CatSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BattleCat.objects.filter(is_published=True).order_by('id')

    def location(self, obj):
        return reverse('cat_detail', args=[obj.slug])


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': {'cats': CatSitemap}}, name='sitemap'),
    path('', include('wiki.urls')), # Перенаправляє всі запити у правильний файл wiki/urls.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
