from django.conf.urls import url
from . import views


urlpatterns = [
	 url(r'^camaras_list/$', views.camara_list, name='listar_camaras'),
	 url(r'^generate_pdf/$', views.generate_pdf, name='generate_pdf'),
	 url(r'^camaras_list_for_reports/$', views.get_all_boxes, name='listar_camaras_relatorios'),
	  url(r'^all_reports_list/$', views.get_all_boxes, name='listar_camaras_completas'),
	 url(r'^transport_list_for_reports/(?P<camara_name>.*)$', views.get_transports_from_box, name='transport_list_reports'),
	 url(r'^reports_list/(?P<camara_name>.*)/(?P<transport_id>[0-9]+)$', views.reports_list, name='reports_list'),
	 url(r'^camaras_cadastro/$', views.camara_cadastro, name='camaras_cadastro')
]