from django.test import TestCase
from django.core.urlresolvers import reverse
import requests


class CamaraTest(TestCase):

    def setUp(self):
        self.headers = {'content-type': 'application/json'}
        self.username = 'teste'
        self.payload = "{\n\t\"username\": \"teste\",\n\t\"password\": \"teste\"\n}"
        self.url = "https://transports-rest-api.herokuapp.com/auth"

        self.token = requests.post(
        self.url, data=self.payload, headers=self.headers).json()

        self.url_cadastro = reverse('camara:camaras_cadastro')
        self.url_list = reverse('camara:listar_camaras')
        self.url_all_boxes = reverse('camara:relatorio_geral')

    def test_cadastro(self):
        session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session.save()
        response = self.client.get(self.url_cadastro)
        self.assertEqual(response.status_code, 200 or 302)

    def test_list(self):
        session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session.save()
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code,  200 or 302)

    def test_get_all_boxes(self):
        session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session.save()
        response = self.client.get(self.url_all_boxes)
        self.assertEqual(response.status_code,  200 or 302)
