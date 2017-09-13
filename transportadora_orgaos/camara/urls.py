from django.conf.urls import url
from .views import *





urlpatterns = [
	 url(r'^camaras/', CamaraView.as_view()),
	 url(r'^cadastro/camaras/', CamarasCadastro.as_view()),
]