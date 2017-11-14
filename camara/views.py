# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from usuario.view import get_acess_level


class CamaraForm(ModelForm):
    class Meta:
        model = Camara
        fields = ['name']

def camara_list(request, template_name='page_camaras_list.html'):

    if 'token' in request.session:
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
    else:
        return redirect('usuario:login')


def camara_delete(request, camara_name, template_name="page_camaras_list.html"):
    	
    payload = ""
    headers = {'content-type': 'application/json'}

    #Deletar câmara específica
    url = "https://transports-rest-api.herokuapp.com/box/" + camara_name
    response = requests.request("DELETE", url, data=payload, headers=headers)

    return redirect('camara:listar_camaras')

def get_all_boxes(request, template_name='all_camaras_reports.html'):
    if 'token' in request.session:
        level = get_acess_level(request)
        if 'Administrador' in level["access_level"]:
            url = "https://transports-rest-api.herokuapp.com/boxes"
            headers = {'content-type': 'application/json'}

            camaras = requests.request("GET", url, headers=headers)
            camaras_dict = camaras.json()['boxes']
            return render(request, template_name, {'camaras_dict':camaras_dict})
        else:
            return redirect('usuario:denied')
    else:
        return redirect('usuario:login')

def get_transports_from_box(request, camara_name, template_name="transports_list_for_reports.html"):
    if 'token' in request.session:
        level = get_acess_level(request)
        if 'Administrador' in level["access_level"]:
            url = "https://transports-rest-api.herokuapp.com/box/" + camara_name
            headers = {'content-type': 'application/json'}
            camara_transports = requests.request("GET", url, headers=headers).json()['transports']

            return render(request, template_name, {'camara_transports' : camara_transports})
        else:
            return redirect('usuario:denied')
    else:
        return redirect('usuario:login')

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
