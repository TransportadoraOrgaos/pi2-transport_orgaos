from django.shortcuts import render, render_to_response, redirect
from usuario.forms import UsuarioModelForm, UsuarioLoginForm
from django.views.generic import TemplateView
import requests
import json


class Index(TemplateView):
    template_name = 'base.html'


def cadastro(request, template_name='usuario/cadastro.html'):
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

		if 'error_message' or 'message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict})
		else:
			return redirect('usuario:cadastro')
	return render(request, template_name, {'form': form})

def do_login(request, template_name='usuario/login.html'):
	form = UsuarioLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		headers = {'content-type': 'application/json'}
		payload = "{\n\t\"username\": \""+ username +"\",\n\t\"password\": \""+ password +"\"\n}"
		url = "https://transports-rest-api.herokuapp.com/auth"
		response = requests.post(url, data=payload, headers=headers)

		# import ipdb; ipdb.set_trace()

		if 'error_message' or 'message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict})
		elif 'access_token' in response.json():
			token = response.json()
			return redirect('home')
	return render(request, template_name, {'form': form})

# def do_logout(request):
# 	logout(request)
# 	return redirect('/login')

def list(request, template_name='usuario/list.html'):
	url = "https://transports-rest-api.herokuapp.com/users"
	headers = {'content-type': 'application/json'}

	users = requests.request("GET", url, headers=headers)
	users_dict = users.json()['users']
	
	return render(request, template_name, {'users_dict':users_dict})