from django.conf.urls import url
from . import views


urlpatterns = [
	 url(r'^camaras_list/$', views.camara_list, name='listar_camaras'),
	 url(r'^camaras_cadastro/$', views.camara_cadastro, name='camaras_cadastro'),
	 url(r'^camara_delete/(?P<camara_name>.*)$', views.camara_delete, name='camara_delete')
]