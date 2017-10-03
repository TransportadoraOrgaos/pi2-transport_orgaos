from django.shortcuts import render, render_to_response, redirect
from usuario.forms import UsuarioModelForm
from django.views.generic import TemplateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class Index(TemplateView):
    template_name = 'base.html'

@login_required
def cadastro(request):
	form = UsuarioModelForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
	return render(request, 'usuario/cadastro.html', context)

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/home')
	return render(request, 'camaras_list.html')

def do_logout(request):
	logout(request)
	return redirect('/login')