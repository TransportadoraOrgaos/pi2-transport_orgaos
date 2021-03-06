from django.test import TestCase
from django.core.urlresolvers import reverse
import requests

class PagesTest(TestCase):

    def setUp(self):
        self.url_login = reverse('usuario:login')
        self.url_cadastro = reverse('usuario:cadastro')
        self.url_denied = reverse('usuario:denied')
        self.url_list = reverse('usuario:list')
        self.url_del_user = reverse('usuario:user_delete', kwargs={'users_username': 'aaaa'})
        self.url_do_logout = reverse('usuario:logout')

        self.headers = {'content-type': 'application/json'}
        self.username = 'teste'
        self.password = 'teste'
        self.username_usuario = 'usuario'
        self.payload = "{\n\t\"username\": \"teste\",\n\t\"password\": \"teste\"\n}"
        self.url = "https://transports-rest-api.herokuapp.com/auth"
       
        self.token = requests.post(self.url, data=self.payload, headers=self.headers).json()


    def test_cadastro(self):
        session = self.client.session
        session['password'] = self.password
        response = self.client.get(self.url_cadastro)
        self.assertEqual(response.status_code, 302)

    def test_cadastro_user(self):
    	session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] = self.password
        session.save()

        form_data = {'username': 'aaaa','password': '12345', 'email': 'aaa@aa.com', 'access_level': 'Administrador'}

        response = self.client.post(self.url_cadastro, form_data)
        self.assertEqual(response.status_code, 200 or 302)

    def test_cadastro_sem_access_level(self):
    	session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] = self.password
        session.save()

        form_data = {'username': 'aaaa','password': '12345', 'email': 'aaa@aa.com', 'access_level': 'Administrador'}

        response = self.client.post(self.url_cadastro, form_data)
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        session = self.client.session
        session['password'] = self.password
        response = self.client.get(self.url_login)
        self.assertEqual(response.status_code, 200)


    def test_denied(self):
        session = self.client.session
        session['password'] = self.password
    	response = self.client.get(self.url_denied)
    	self.assertEqual(response.status_code, 200)

    def test_list(self):
    	session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] = self.password
        session.save()
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, 200)

    def test_list_sem_token(self):
        session = self.client.session
        session['password'] = self.password
    	response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 302)

    def test_list_sem_access_level(self):
    	session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] = self.password
        session.save()

    	response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200 or 302)


    def test_login_user(self):
    	form_data = {'username': 'teste','password': 'teste'}
        
        response = self.client.post(self.url_login, form_data)
        
        self.assertEqual(response.status_code, 302)

    def test_login_user_invalid(self):
        session = self.client.session
        session['password'] = self.password
    	form_data = {'username': 'aaaa','password': '54321'}
        
        response = self.client.post(self.url_login, form_data)
        
        self.assertEqual(response.status_code, 200)

    def test_del_user(self):
    	session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] = self.password
        session.save()

        form_data = {'username': 'aaaa','password': '12345', 'email': 'aaa@aa.com', 'access_level': 'Administrador'}

        response = self.client.post(self.url_cadastro, form_data)
        self.assertEqual(response.status_code, 200)

        response = self.client.delete(self.url_del_user)

        self.assertEqual(response.status_code, 302)

    def test_del_user_sem_token(self):
        session = self.client.session
        session['password'] = self.password
    	
        form_data = {'username': 'aaaa','password': '12345', 'email': 'aaa@aa.com', 'access_level': 'Administrador'}

        response = self.client.post(self.url_cadastro, form_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.delete(self.url_del_user)

        self.assertEqual(response.status_code, 302)

    def test_del_user_sem_access_level(self):
    	session = self.client.session
        session['token'] = self.token
        session['username'] = self.username
        session['password'] = self.password
        session.save()

        form_data = {'username': 'aaaa','password': '12345', 'email': 'aaa@aa.com', 'access_level': 'Administrador'}

        response = self.client.post(self.url_cadastro, form_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.delete(self.url_del_user)

        self.assertEqual(response.status_code, 302)

    def test_do_logout(self):
    	response = self.client.post(self.url_do_logout)
        self.assertEqual(response.status_code, 302)
