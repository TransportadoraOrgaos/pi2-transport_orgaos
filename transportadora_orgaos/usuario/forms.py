# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from usuario.models import Usuario

class UsuarioModelForm(ModelForm):
	class Meta:
		ADMINISTRADOR = "Administrador"
		TRASPORTADOR = "Transportador"
		USUARIO = "Usuario"
		ACCESS_CHOICES = (
		(ADMINISTRADOR, 'Administrador'), 
		(TRASPORTADOR, 'Transportador'),
		(USUARIO, 'Usuario'),
		)

		model = Usuario
		fields = ['username', 'password', 'email', 'access_level']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
			'email': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
			'password': forms.PasswordInput(attrs={'class': 'form_control', 'maxlength': 50}),
			'access_level': forms.Select(choices= ACCESS_CHOICES, attrs={'class': 'form_control'}),
		}

class UsuarioLoginForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ['username', 'password']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
			'email': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
		}