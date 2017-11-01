# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests
from reportlab.pdfgen import canvas
from django.http import HttpResponse


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

def get_all_reports(request, template_name='camaras_list_for_reports.html'):
    url = "https://transports-rest-api.herokuapp.com/boxes"
    headers = {'content-type': 'application/json'}
       
    camaras = requests.request("GET", url, headers=headers)
    camaras_dict = camaras.json()['boxes']
    return render(request, template_name, {'camaras_dict':camaras_dict})

def get_transports_from_box(request, camara_name, template_name="transports_list_for_report.html"):
	url = "https://transports-rest-api.herokuapp.com/box/" + camara_name
	headers = {'content-type': 'application/json'}
	camara_transports = requests.request("GET", url, headers=headers)
	transports_dict = camara_transports.json()['transports']

	return render(request, template_name, {'transports_dict':transports_dict})