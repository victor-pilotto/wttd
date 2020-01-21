from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.core.models import Speaker


class SpeakerDetailGet(TestCase):
    def setUp(self) -> None:
        Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            website='http://hbn.link/hopper-site',
            photo='http://hbn.link/hopper-pic',
            description='Programadora e almirante',
        )
        self.response = self.client.get(r('speaker_detail', slug='grace-hopper'))

    def test_get(self):
        """GET should return status 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        """Speaker must be in context"""
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)