from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests
import json

class CamaraForm(ModelForm):
	class Meta:
		model = Camara
		fields = ['name', 'responsible', 'organ']

def camara_list(request, template_name='camaras_list.html'):
	url = "https://transports-rest-api.herokuapp.com/transports"
	headers = {'content-type': 'application/json'}

	camaras = requests.request("GET", url, headers=headers)
	camaras_dict = camaras.json()['transports']
	
	return render(request, template_name, {'camaras_dict':camaras_dict})

def camara_cadastro(request, template_name='camaras_cadastro.html'):
	 
	form = CamaraForm(request.POST or None)
	
	headers = {'content-type': 'application/json'}
	
	if form.is_valid():
		responsible = form.cleaned_data['responsible']
		organ = form.cleaned_data['organ']
		payload = "{\n\t\"responsible\": \""+ responsible +"\",\n\t\"organ\": \""+ organ +"\"\n}"
		url = "https://transports-rest-api.herokuapp.com/transport/" + form.cleaned_data['name']
		response = requests.request("POST", url, data=payload, headers=headers)

		if 'error_message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict})
		else:
			return redirect('camara:listar_camaras')
	return render(request, template_name, {'form': form})

def camara_info(request, camara_id, template_name='camara_info.html'):
	url = "https://transports-rest-api.herokuapp.com/report/" + str(camara_id)
	headers = {
		'content-type': 'application/json', 
		'authorization': "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MDczMDIxNzAs" 
		+"Im5iZiI6MTUwNzMwMjE3MCwiaWRlbnRpdHkiOjEsImV4cCI6MTUwNzMwMjQ3MH0.8e5Dgf79L4bIUGHdwX"
		+"--NgkSWzCz96UFuqvBKZ-jk3g"
    }

	camara_reports = requests.request("GET", url, headers=headers).json()['reports']

	return render(request, template_name, {'camara_reports':camara_reports})

	
