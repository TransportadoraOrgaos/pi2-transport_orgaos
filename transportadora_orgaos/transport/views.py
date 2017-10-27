# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
import requests


class TransportForm(ModelForm):
    class Meta():
        model = Transport
        fields = ['organ', 'responsible']
        
def transport_cadastro(request, box_id, template_name='page_transport_cadastro.html'):
    form = TransportForm(request.POST or None)

    if form.is_valid():
        transport_id = 1
        transport_id+=1

        headers = {'content-type': 'application/json'}
        url = "https://transports-rest-api.herokuapp.com/transport/"+str(transport_id)

        organ = form.cleaned_data['organ']
        responsible = form.cleaned_data['responsible']

        payload = "{\n\t\"organ\": \"" + organ + "\",\n\t\"responsible\": \""+ responsible +"\",\n\t\"box_id\": "+ box_id +"\n}"
        

        response = requests.request("POST", url, data=payload, headers=headers)

        if 'error_message' or 'message' in response.json():
            response_dict = response.json()
            return render(request, template_name, {'form': form, 'response_dict': response_dict})
        else:
            return redirect('camara:listar_camaras')
    return render(request, template_name, {'form' : form})



def transport_info(request, transport_id, template_name="page_reports.html"):

    #RECUPERAR REPORTS DO TRANSPORT_ID
    url = "https://transports-rest-api.herokuapp.com/report/" + transport_id
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

    #RECUPERAR DADOS DO TRANSPORT_ID
    url = "https://transports-rest-api.herokuapp.com/transport/" + transport_id
    headers = {'content-type': 'application/json'}

    transport = requests.request("GET", url, headers=headers).json()

    #RECUPERAR DADOS DO BOX_ID
    
    return render(request, template_name, {'transport_reports':transport_reports, 'transport':transport ,'temperaturas':temperaturas})