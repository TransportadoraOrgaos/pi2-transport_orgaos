# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from usuario.models import Usuario

class UsuarioModelForm(ModelForm):
    ADMINISTRADOR = "Administrador"
    TRASPORTADOR = "Transportador"
    USUARIO = "Usuario"
    ACCESS_CHOICES = (
    (ADMINISTRADOR, 'Administrador'), 
    (TRASPORTADOR, 'Transportador'),
    (USUARIO, 'Usuário'),
    )
    access_level = forms.ChoiceField(choices= ACCESS_CHOICES)

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email', 'access_level']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
            'email': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
            'password': forms.PasswordInput(attrs={'class': 'form_control', 'maxlength': 50})
        }

class UsuarioLoginForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
            'email': forms.TextInput(attrs={'class': 'form_control', 'maxlength': 50}),
        }