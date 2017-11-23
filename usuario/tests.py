from django.test import TestCase

class PagesTest(TestCase):
    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_cadastro(self):
        response = self.client.get('/cadastro')
        self.assertEqual(response.status_code, 302)