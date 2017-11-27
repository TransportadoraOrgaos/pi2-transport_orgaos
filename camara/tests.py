from django.test import TestCase
from django.core.urlresolvers import reverse


class CamaraTest(TestCase):

    def setUp(self):
        self.url_cadastro = reverse('camara:camaras_cadastro')
        self.url_list = reverse('camara:listar_camaras')
        self.url_all_boxes = reverse('camara:relatorio_geral')

    def test_cadastro(self):
        response = self.client.get(self.url_cadastro)
        self.assertEqual(response.status_code, 302)

    def test_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 302)

    def test_get_all_boxes(self):
        response = self.client.get(self.url_all_boxes)
        self.assertEqual(response.status_code, 302)
        
