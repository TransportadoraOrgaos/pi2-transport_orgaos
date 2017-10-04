from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests
import json

class CamaraForm(ModelForm):
	class Meta:
		model = Camara
		fields = ['name']

def camara_list(request, template_name='camaras_list.html'):
	url = "https://transports-rest-api.herokuapp.com/transports"
	headers = {'content-type': 'application/json'}

	camaras = requests.request("GET", url, headers=headers)
	camaras_dict = camaras.json()['transports']
	
	return render(request, template_name, {'camaras_dict':camaras_dict})

def camara_cadastro(request, template_name='camaras_cadastro.html'):
	 
	form = CamaraForm(request.POST or None)
	payload = ""
	headers = {'content-type': 'application/json'}
	
	if form.is_valid():
		url = "https://transports-rest-api.herokuapp.com/transport/" + form.cleaned_data['name']
		response = requests.request("POST", url, data=payload, headers=headers)
		if 'message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict})
		else:
			return redirect('camara:listar_camaras')
	return render(request, template_name, {'form': form})
