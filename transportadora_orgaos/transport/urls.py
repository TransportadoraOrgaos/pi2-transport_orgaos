from django.conf.urls import url
from . import views


urlpatterns = [
	 url(r'^transport_cadastro/(?P<box_id>[0-9]+)$', views.transport_cadastro, name='transport_cadastro'),
	 url(r'^transport__info/(?P<transport_id>[0-9]+)/(?P<camara_name>.*)$', views.transport_info, name='transport_info')
]