from django.shortcuts import render, render_to_response
from usuario.forms import UsuarioModelForm
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'base.html'

def cadastro(request):
	form = UsuarioModelForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
	return render(request, 'usuarios/cadastro.html', context)
