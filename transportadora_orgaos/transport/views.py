# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
from django.conf import settings
import requests


class TransportForm(ModelForm):
    class Meta():
        model = Transport
        fields = ['organ', 'responsible']
        
def transport_cadastro(request, box_id, camara_name, template_name='page_transport_cadastro.html'):
    form = TransportForm(request.POST or None)
    
    if 'token' in request.session:
        
        if form.is_valid():
        

            url = "https://transports-rest-api.herokuapp.com/createtransport"

            organ = form.cleaned_data['organ']
            responsible = form.cleaned_data['responsible']

            payload = "{\n\t\"organ\": \"" + organ + "\",\n\t\"responsible\": \""+ responsible +"\",\n\t\"box_id\": "+ box_id +"\n}"
            
            response = requests.request("POST", url, data=payload, headers=headers)

            if 'error_message' in response.json():
                response_dict = response.json()
                return render(request, template_name, {'form': form, 'response_dict': response_dict})
            else:
                return redirect("camara:listar_camaras")
        return render(request, template_name, {'form' : form, 'camara_info' : camara_info})
    else:
        return redirect('usuario:login')


def transport_info(request, transport_id, camara_name, template_name="page_reports.html"):

    if 'token' in request.session:
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
        
        return render(request, template_name, {'transport_reports':transport_reports, 'transport':transport ,'temperaturas':temperaturas, 'camara_name':camara_name})
    else:
        return redirect('usuario:login')
    
