# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests
import json


class CamaraForm(ModelForm):
	class Meta:
		model = Camara
		fields = ['name']

def camara_list(request, template_name='page_camaras_list.html'):
	url = "https://transports-rest-api.herokuapp.com/boxes"
	headers = {'content-type': 'application/json'}

	camaras = requests.request("GET", url, headers=headers)
	camaras_dict = camaras.json()['boxes']
	
	return render(request, template_name, {'camaras_dict':camaras_dict})


def camara_cadastro(request, template_name='page_camara_cadastro.html'):

	form = CamaraForm(request.POST or None)
	
	if form.is_valid():
		headers = {'content-type': 'application/json'}
		payload = ""
		url = "https://transports-rest-api.herokuapp.com/box/" + form.cleaned_data['name']
		response = requests.post(url, data=payload, headers=headers)

		if 'error_message' or 'message' in response.json():
			response_dict = response.json()
			return render(request, template_name, {'form': form, 'response_dict': response_dict})
		else:
			return redirect('camara:listar_camaras')
	return render(request, template_name, {'form': form})

def camara_info(request, camara_id, template_name='camaras_list.html'):
	headers = {'content-type': 'application/json'}

	#Recupera todos os reports da camara_id
	url = "https://transports-rest-api.herokuapp.com/report/" + str(camara_id)
	camara_reports = requests.request("GET", url, headers=headers).json()['reports']

	#Recupera as informações da camara_id
	#url = "https://transports-rest-api.herokuapp.com/transports"
	#camaras = requests.request("GET", url, headers=headers)
	#camara = camaras.json()['transports'][int(camara_id)-1]

	#Recupera as temperaturas da camara_id para a construção do gráfico
	temperaturas = []
	i = 0
	for temperatura in camara_reports:
		temperaturas.append([i, camara_reports[i]['temperature']])
		i += 1
	
	print(temperaturas)
	
	return render(request, template_name, {'camara_reports':camara_reports, 'temperaturas':temperaturas})