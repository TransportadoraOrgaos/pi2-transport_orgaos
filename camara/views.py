# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from usuario.views import get_acess_level

from weasyprint import HTML

class CamaraForm(ModelForm):
    class Meta:
        model = Camara
        fields = ['name']

def recupera_token(request):
    #RECUPERAR O NOVO TOKEN DA API
    headers = {'content-type': 'application/json'}
    url_access = "https://transports-rest-api.herokuapp.com/auth"
    payload_access = "{\n\t\"username\": \""+ request.session['username'] +"\",\n\t\"password\": \""+ request.session['password'] +"\"\n}"
    response = requests.post(url_access, data=payload_access, headers=headers)
    token = response.json()
    request.session['token'] = token

def camara_list(request, template_name='page_camaras_list.html'):

    if 'token' in request.session:
        recupera_token(request)

        url = "https://transports-rest-api.herokuapp.com/boxes"
        headers = {'content-type': 'application/json', 'authorization': 'jwt ' + request.session['token']['access_token']}
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

    recupera_token(request)
    	
    payload = ""
    headers = {'content-type': 'application/json', 'authorization': 'jwt ' + request.session['token']['access_token']}

    #Deletar câmara específica
    url = "https://transports-rest-api.herokuapp.com/box/" + camara_name
    response = requests.request("DELETE", url, data=payload, headers=headers)

    return redirect('camara:listar_camaras')

def get_all_boxes(request, template_name='all_camaras_reports.html'):
    if 'token' in request.session:
        recupera_token(request)
        level = get_acess_level(request)
        if 'Administrador' in level["access_level"]:
            url = "https://transports-rest-api.herokuapp.com/boxes"
            headers = {'content-type': 'application/json', 'authorization': 'jwt ' + request.session['token']['access_token']}

            
            camaras = requests.request("GET", url, headers=headers)
            
            
            camaras_dict = camaras.json()['boxes']
            return render(request, template_name, {'camaras_dict':camaras_dict})
        else:
            return redirect('usuario:denied')
    else:
        return redirect('usuario:login')

def get_transports_from_box(request, camara_name, template_name="transports_list_for_reports.html"):
    if 'token' in request.session:
        recupera_token(request)
        level = get_acess_level(request)
        if 'Administrador' in level["access_level"]:
            url = "https://transports-rest-api.herokuapp.com/box/" + camara_name
            headers = {'content-type': 'application/json', 'authorization': 'jwt ' + request.session['token']['access_token']}
            
            
            camara_transports = requests.request("GET", url, headers=headers).json()['transports']
            

            return render(request, template_name, {'camara_transports' : camara_transports})
        else:
            return redirect('usuario:denied')
    else:
        return redirect('usuario:login')

def generate_pdf(request):
    recupera_token(request)
    url = "https://transports-rest-api.herokuapp.com/boxes"
    headers = {'content-type': 'application/json', 'authorization': 'jwt ' + request.session['token']['access_token']}

    camaras = requests.request("GET", url, headers=headers)
    camaras_dict = camaras.json()['boxes']

    
    
    html_string = render_to_string(
        'pdf_template.html', {'camaras_dict': camaras_dict})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/reports.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('reports.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reports.pdf"'
        return response

    return response
