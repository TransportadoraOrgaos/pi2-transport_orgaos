from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^cadastro$', views.cadastro, name='cadastro'),
	url(r'^login$', views.do_login, name='login'),
	url(r'^logout$', views.do_logout, name='logout'),
	url(r'^list$', views.list, name='list'),
]