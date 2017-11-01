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

def get_all_boxes(request, template_name='all_reports_list.html'):
    url = "https://transports-rest-api.herokuapp.com/boxes"
    headers = {'content-type': 'application/json'}
       
    camaras = requests.request("GET", url, headers=headers)
    camaras_dict = camaras.json()['boxes']
    return render(request, template_name, {'camaras_dict':camaras_dict})

def get_transports_from_box(request, camara_name, template_name="transports_list_for_reports.html"):
	url = "https://transports-rest-api.herokuapp.com/box/" + camara_name
	headers = {'content-type': 'application/json'}
	camara_transports = requests.request("GET", url, headers=headers)
	transports_dict = camara_transports.json()['transports']

	return render(request, template_name, {'transports_dict':transports_dict})

def reports_list(request, camara_name, transport_id, template_name="reports_list.html"):
	url = "https://transports-rest-api.herokuapp.com/box/" + camara_name + transport_id
	headers = {'content-type': 'application/json'}
	response = requests.request("GET", url, headers=headers)
	reports_dict = response.json()

	print(response.text)
	return render(request, template_name, {'reports_dict':reports_dict})

def generate_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(0,0, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
