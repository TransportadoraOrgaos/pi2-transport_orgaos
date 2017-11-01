from django.conf.urls import url
from . import views


urlpatterns = [
	 url(r'^camaras_list/$', views.camara_list, name='listar_camaras'),
	 url(r'^camaras_list_for_reports/$', views.get_all_reports, name='listar_camaras_relatorios'),
	 url(r'^transport_list_for_reports/(?P<camara_name>.*)$', views.get_transports_from_box, name='transport_list_reports'),
	 url(r'^camaras_cadastro/$', views.camara_cadastro, name='camaras_cadastro')
]