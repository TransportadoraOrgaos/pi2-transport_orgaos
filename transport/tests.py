from django.test import TestCase
from django.core.urlresolvers import reverse
import requests

class TransportTest(TestCase):    

    def setUp(self):
        self.headers = {'content-type': 'application/json'}
        self.username = 'teste'
        self.password = 'teste'
        self.payload = "{\n\t\"username\": \"teste\",\n\t\"password\": \"teste\"\n}"
        self.url = "https://transports-rest-api.herokuapp.com/auth"
       
        self.token = requests.post(self.url, data=self.payload, headers=self.headers).json()

        self.url_cadastro = reverse('transport:transport_cadastro', kwargs={'box_id': 1, 'camara_name':'camara 1'})
        self.url_info = reverse('transport:transport_info', kwargs={'transport_id':2, 'camara_name':'camara 2'})

    def test_transport_cadastro(self):
        session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] =self.password
        session.save()
        response = self.client.get(self.url_cadastro)
        
        self.assertEqual(response.status_code,  200 or 302)
    
    def test_transport_info(self):
        session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] =self.password
        session.save()
        response = self.client.get(self.url_info)

        self.assertEqual(response.status_code,  200 or 302)
