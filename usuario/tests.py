from django.test import TestCase
from django.core.urlresolvers import reverse

import django
django.setup()

class PagesTest(TestCase):

    def setUp(self):
        self.url_login = reverse('usuario:login')
        self.url_cadastro = reverse('usuario:cadastro')


    def test_login(self):
        response = self.client.get(self.url_login)
        self.assertEqual(response.status_code, 200)

    def test_cadastro(self):
        response = self.client.get(self.url_cadastro)
        self.assertEqual(response.status_code, 302)