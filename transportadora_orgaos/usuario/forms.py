# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UsuarioModelForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'email', 'password']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 100}),
			'first_name': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 100}),
			'email': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 100}),
			'password': forms.PasswordInput(attrs={'class': 'form_control', 'maxlength': 100}),
		}

def save(self, commit="True"):
	user = super(UsuarioModelForm, self).save(commit="false")
	user.set_password(self.cleaned_data['password'])
	if commit:
		user.save()
	return user
