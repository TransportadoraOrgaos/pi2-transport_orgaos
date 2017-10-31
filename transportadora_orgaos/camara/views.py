# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests


class CamaraForm(ModelForm):
	class Meta:
		model = Camara
		fields = ['name']

def camara_list(request, template_name='page_camaras_list.html'):
	url = "https://transports-rest-api.herokuapp.com/boxes"
	headers = {'content-type': 'application/json'}
	payload = ""

	camaras = requests.request("GET", url, headers=headers)
	camaras_dict = camaras.json()['boxes']

	form = CamaraForm(request.POST or None)
	
	if form.is_valid():
		url = "https://transports-rest-api.herokuapp.com/box/" + form.cleaned_data['name']
		response = requests.post(url, data=payload, headers=headers)

		if 'error_message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict, 'camaras_dict':camaras_dict})
		else:
			return redirect('camara:listar_camaras')
	return render(request, template_name, {'camaras_dict':camaras_dict, 'form':form})


def camara_delete(request, camara_name, template_name="page_camaras_list.html"):
	
	payload = ""
	headers = {'content-type': 'application/json'}

	#Deletar câmara específica
	url = "https://transports-rest-api.herokuapp.com/box/" + camara_name
	response = requests.request("DELETE", url, data=payload, headers=headers)

	return redirect('camara:listar_camaras')
