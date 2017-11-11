from django.conf.urls import url
from . import views


urlpatterns = [
	 url(r'^camaras_list/$', views.camara_list, name='listar_camaras'),
	 url(r'^camara_delete/(?P<camara_name>.*)$', views.camara_delete, name='camara_delete'),
	 url(r'^generate_pdf/$', views.generate_pdf, name='generate_pdf'),
     url(r'^camaras_list_for_reports/$', views.get_all_boxes, name='listar_camaras_relatorios'),
	 url(r'^all_camaras_reports/$', views.get_all_boxes, name='relatorio_geral'),
	 url(r'^transports_list_for_reports/(?P<camara_name>.*)$', views.get_transports_from_box, name='listar_transports_relatorios'),
	#  url(r'^reports_list/(?P<camara_name>.*)/(?P<transport_id>[0-9]+)$', views.reports_list, name='reports_list'),
	 url(r'^camaras_cadastro/$', views.camara_list, name='camaras_cadastro')
]