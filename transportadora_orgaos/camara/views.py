from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests


class CamaraForm(ModelForm):
	class Meta:
		model = Camara
		fields = ['name']

def camara_list(request, template_name='camaras_list.html'):
	camara = Camara.objects.all()
	camaras = {'lista_camaras' : camara}
	return render(request, template_name, camaras)

def camara_cadastro(request, template_name='camaras_cadastro.html'):
	 
	form = CamaraForm(request.POST or None)
	payload = ""
	headers = {'content-type': 'application/json'}
	
	if form.is_valid():
		url = "https://transports-rest-api.herokuapp.com/transport/" + form.cleaned_data['name']
		response = requests.request("POST", url, data=payload, headers=headers)
		return redirect('camara:listar_camaras')
	return render(request, template_name, {'form': form})
