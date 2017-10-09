from django.shortcuts import render, render_to_response, redirect
from usuario.forms import UsuarioModelForm
from django.views.generic import TemplateView
import requests
import json


class Index(TemplateView):
    template_name = 'base.html'


def cadastro(request, template_name='usuario/cadastro.html'):
	form = UsuarioModelForm(request.POST or None)
	import ipdb; ipdb.set_trace()
	
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']

		headers = {'content-type': 'application/json'}
		payload = "{\n\t\"username\": \""+ username +"\",\n\t\"password\": \""+ password +"\", \n\t\"email\": \""+ email +"\"\n}"
		url = "https://transports-rest-api.herokuapp.com/register"
		response = requests.post(url, data=payload, headers=headers)

		if 'error_message' or 'message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict})
		else:
			return redirect('usuario:cadastro')
	return render(request, template_name, {'form': form})

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/home')
	return render(request, 'camaras_list.html')

def do_logout(request):
	logout(request)
	return redirect('/login')