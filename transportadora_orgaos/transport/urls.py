from django.conf.urls import url
from . import views


urlpatterns = [
	 url(r'^transport_cadastro/(?P<box_id>[0-9]+)$', views.transport_cadastro, name='transport_cadastro'),
	 url(r'^transport_list/$', views.transport_list, name='listar_transports'),
]