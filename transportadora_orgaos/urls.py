"""transportadora_orgaos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from usuario.views import Index
from camara.views import camara_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', camara_list, name='home'),
    url(r'^', include('usuario.urls', namespace='usuario', app_name='usuario')),
    url(r'^', include('camara.urls', namespace='camara', app_name='camara')),
    url(r'^', include('transport.urls', namespace='transport', app_name='transport'))
]
