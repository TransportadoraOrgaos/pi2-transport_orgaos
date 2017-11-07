from django.shortcuts import render, render_to_response, redirect
from usuario.forms import UsuarioModelForm, UsuarioLoginForm
from django.views.generic import TemplateView
import requests
import json


class Index(TemplateView):
    template_name = 'base.html'


def cadastro(request, template_name='usuario/cadastro.html'):
	if 'token' in request.session:
		level = get_acess_level(request)
		if 'Administrador' in level["access_level"]:
			form = UsuarioModelForm(request.POST or None)
			
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				email = form.cleaned_data['email']
				access_level = form.cleaned_data['access_level']

				headers = {'content-type': 'application/json'}
				payload = "{\n\t\"username\": \""+ username +"\",\n\t\"password\": \""+ password +"\", \n\t\"email\": \""+ email +"\", \n\t\"access_level\": \""+ access_level +"\"\n}"
				url = "https://transports-rest-api.herokuapp.com/user"
				response = requests.post(url, data=payload, headers=headers)

				if 'error_message' in response.json():
					response_dict = response.json()
					return render(request, template_name, {'form': form, 'response_dict': response_dict})
				else:
					return redirect('usuario:list')
			return render(request, template_name, {'form': form})
		else:
			return redirect('usuario:denied')
	else:
		return redirect('usuario:login')

def do_login(request, template_name='usuario/login.html'):
	form = UsuarioLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		headers = {'content-type': 'application/json'}
		payload = "{\n\t\"username\": \""+ username +"\",\n\t\"password\": \""+ password +"\"\n}"
		url = "https://transports-rest-api.herokuapp.com/auth"
		response = requests.post(url, data=payload, headers=headers)

		if 'error_message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict})
		elif 'access_token' in response.json():
			token = response.json()
			request.session['token'] = token
			request.session['username'] = username
			access_level = get_acess_level(request)
			request.session['access_level'] = access_level['access_level']
			import ipdb; ipdb.set_trace()
			return redirect('home')
	return render(request, template_name, {'form': form})

def formView(request):
	if request.session.has_key('token'):
		token = request.session['token']
		return render(request, 'home', {"token" : token})
	else:
		return render(request, 'usuario/login.html', {})

def do_logout(request):
	try:
		del request.session['token']
	except:
		pass
	return redirect('usuario:login')

def list(request, template_name='usuario/list.html'):
	if 'token' in request.session:
		url = "https://transports-rest-api.herokuapp.com/users"
		headers = {'content-type': 'application/json'}

		users = requests.request("GET", url, headers=headers)
		users_dict = users.json()['users']
		
		return render(request, template_name, {'users_dict':users_dict})
	else:
		return redirect('usuario:login')

def del_User(request, users_username, template_name='usuario/list.html'):
	
	headers = {'content-type': 'application/json'}
	payload = "{\n\t\"username\": \""+ users_username +"\"\n}"
	url = "https://transports-rest-api.herokuapp.com/user"
	
	response = requests.request("DELETE", url, data=payload, headers=headers)

	return redirect('usuario:list')

def get_acess_level(request):

	url = "https://transports-rest-api.herokuapp.com/user_access/" + request.session['username']
	headers = {'content-type': 'application/json'}
	response = requests.request("GET", url, headers=headers)

	if 'access_level' in response.json():
		level = response.json()

	return level

def denied(request):
	template_name = 'denied.html'
	return render(request, template_name)