from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Territory


class TerritoriesSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return ['territories']

    def location(self, item):
        return reverse(item)


class TerritorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Territory.objects.all()

    def location(self, obj: Territory) -> str:
        return reverse('territory', args=(obj.code,))
