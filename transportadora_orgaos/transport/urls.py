from django.conf.urls import url
from . import views


urlpatterns = [
	 url(r'^transport_cadastro/$', views.transport_cadastro, name='transport_cadastro'),
]