from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name='Victor Pilotto', cpf='12345678901',
                    email='teste@teste.com.br', phone='19-98888-3333')
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmacão de inscricão'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'teste@teste.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Victor Pilotto',
            '12345678901',
            'teste@teste.com.br',
            '19-98888-3333'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
