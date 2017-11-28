# -*-encoding: utf-8 -*-

from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect
from django.conf import settings
from usuario.views import get_acess_level
import requests


class TransportForm(ModelForm):
    CHOICES = (('Rim', 'Rim'),('Pancreas', 'Pancreas'),('Cornea', 'Córnea'))
    organ = forms.ChoiceField(choices=CHOICES)
    class Meta():
        model = Transport
        fields = ['organ', 'responsible']
        
def transport_cadastro(request, box_id, camara_name, template_name='page_transport_cadastro.html'):
    form = TransportForm(request.POST or None)

    headers = {'content-type': 'application/json', 'authorization': 'jwt ' + request.session['token']['access_token']}
    url = "https://transports-rest-api.herokuapp.com/box/" +camara_name

    camara_info = requests.request("GET", url, headers=headers).json()
    
    if 'token' in request.session:
        level = get_acess_level(request)
        if 'Administrador' or 'Transportador' in level["access_level"]:

            if form.is_valid():
        

                url = "https://transports-rest-api.herokuapp.com/createtransport"

                organ = form.cleaned_data['organ']
                responsible = form.cleaned_data['responsible']

                payload = "{\n\t\"organ\": \"" + organ + "\",\n\t\"responsible\": \""+ responsible +"\",\n\t\"box_id\": "+ box_id +"\n}"
            
                try:
                    response = requests.request("POST", url, data=payload, headers=headers)
                except KeyError, e:
                    return redirect('usuario:login')

                if 'error_message' in response.json():
                    response_dict = response.json()
                    return render(request, template_name, {'form': form, 'response_dict': response_dict})
                else:
                    return redirect("camara:listar_camaras")
            return render(request, template_name, {'form' : form, 'camara_info' : camara_info})
        else:
            return redirect('usuario:denied')
    else:
        return redirect('usuario:login')


def transport_info(request, transport_id, camara_name, template_name="page_reports.html"):

    if 'token' in request.session:
        #RECUPERAR REPORTS DO TRANSPORT_ID
        url = "https://transports-rest-api.herokuapp.com/report/" + transport_id
        headers = {'content-type': 'application/json', 'authorization': 'jwt ' + request.session['token']['access_token']}

        try:
            transport_reports = requests.request("GET", url, headers=headers).json()['reports']
        except KeyError, e:
            return redirect('usuario:login')

        temperaturas = []
        i = 0
        for temperatura in transport_reports:
            temperaturas.append([i, transport_reports[i]['temperature']])
            i += 1
        
        latitudes = []
        j = 0
        for latitude in transport_reports:
            latitudes.append(transport_reports[j]['latitude'])
            j += 1
        
        longitudes = []
        k = 0
        for longitude in transport_reports:
            longitudes.append(transport_reports[k]['longitude'])
            k += 1

        #RECUPERAR DADOS DO TRANSPORT_ID
        url = "https://transports-rest-api.herokuapp.com/transport/" + transport_id
        headers = {'content-type': 'application/json'}

        transport = requests.request("GET", url, headers=headers).json()

        #RECUPERAR DADOS DO BOX_ID
        
        return render(request, template_name, {'transport_reports':transport_reports, 
                                            'transport':transport ,
                                            'temperaturas':temperaturas, 
                                            'camara_name':camara_name,
                                            'latitudes':latitudes,
                                            'longitudes':longitudes
                                        })
        
    else:
        return redirect('usuario:login')
    
    return render(request, template_name, {'transport_reports':transport_reports, 'transport':transport ,'temperaturas':temperaturas, 'camara_name':camara_name})
