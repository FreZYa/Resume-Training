from django.test import TestCase
from django.urls import reverse

from core.models import GeneralSetting


class HomePageTests(TestCase):
    def test_home_renders_on_empty_database(self):
        """A fresh install has no settings yet; the page must still render."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_uses_general_settings(self):
        GeneralSetting.objects.create(name='site_title', parameter='My Resume')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['site_title'], 'My Resume')

    def test_unknown_document_slug_returns_404(self):
        response = self.client.get(reverse('redirect_urls', args=['missing']))
        self.assertEqual(response.status_code, 404)
