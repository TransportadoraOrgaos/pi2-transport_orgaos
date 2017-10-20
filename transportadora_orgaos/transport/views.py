# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
#from django.utils import simplejson
import requests
import json

# Create your views here.
class TransportForm(ModelForm):
    class Meta():
        model = Transport
        fields = ['organ', 'responsible']
        
def transport_cadastro(request, box_id, template_name='page_transport_cadastro.html'):
    
    form = TransportForm(request.POST or None)
    if form.is_valid():
        transport_id = 1
        transport_id+=1
        url = "https://transports-rest-api.herokuapp.com/transport/"+str(transport_id)

        organ = form.cleaned_data['organ']
        responsible = form.cleaned_data['responsible']

        payload = "{\n\t\"organ\": \"" + organ + "\",\n\t\"responsible\": \""+ responsible +"\",\n\t\"box_id\": "+ box_id +"\n}"
        print(payload)
        headers = {'content-type': 'application/json'}

        response = requests.request("POST", url, data=payload, headers=headers)

        if 'error_message' or 'message' in response.json():
            response_dict = response.json()
            return render(request, template_name, {'form': form, 'response_dict': response_dict})
        else:
            return redirect('transport:listar_camaras')
    return render(request, template_name, {'form' : form})

def transport_list(request, template_name='page_transports_list.html'):   

    url = "https://transports-rest-api.herokuapp.com/transports"
    headers = {'content-type': 'application/json'}
    transports = requests.request("GET", url, headers=headers)

    transports_dict = transports.json()['transports']

    return render(request, template_name, {'transports_dict' : transports_dict})

def transport_info(request, box_id, template_name="page_reports.html"):

    url = "https://transports-rest-api.herokuapp.com/report/1"
    headers = {
        'content-type': "application/json",
        'authorization': "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MDc5MTc0NzAsImlkZW50aXR5IjoyLCJleHAiOjE1MDc5MTc3NzAsIm5iZiI6MTUwNzkxNzQ3MH0.qsC3Md3L8Jc7WHfjqX5MpZYdtKbkJEiKT6ndpDFM7ho"
        }
    transport_reports = requests.request("GET", url, headers=headers).json()['reports']

    temperaturas = []
    i = 0
    for temperatura in transport_reports:
		temperaturas.append([i, transport_reports[i]['temperature']])
		i += 1
        
    print(temperaturas)
    
    return render(request, template_name, {'transport_reports':transport_reports, 'temperaturas':temperaturas})