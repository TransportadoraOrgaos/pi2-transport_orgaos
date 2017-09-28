from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect


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
	if form.is_valid():
		form.save()
		return redirect('camara:listar_camaras')
	return render(request, template_name, {'form': form})