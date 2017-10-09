# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from usuario.models import Usuario

class UsuarioModelForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ['username', 'password', 'email']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
			'email': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
			'password': forms.PasswordInput(attrs={'class': 'form_control', 'maxlength': 50}),
		}

class UsuarioLoginForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ['username', 'password']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
			'email': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
		}