from django.shortcuts import render
from django.views import View
# Create your views here.


class CamaraView(View):
	"""
	Classe para retornar listas de camaras cadastradas
	"""

	def get(self, request):
		camaras = "anna lari"
		return render(request, "camaras_list.html", {'camaras': camaras})

	def post(self, request):
		pass

class CamarasCadastro(View):
    """
    Classe para cadastro de camaras
    """

    def get(self, request):
		return render(request, "camaras_form.html")

		pass

    def post(self, request):
		pass


		
