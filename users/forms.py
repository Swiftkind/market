from django import forms
from django.core.validators import RegexValidator
from django.core import validators
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import User


class RegisterForm(forms.ModelForm):

	
	class Meta:
		model = User
		fields = ('first_name','last_name','email','password',)

	def clean_email(self):
		email = User.objects.filter(email=self.cleaned_data['email'])

		if email.exists():
			raise forms.ValidationError('Invalid Email Address!')
		return self.cleaned_data['email']


class LoginForm(forms.ModelForm):


	class Meta:
		model = User
		fields = ('email','password')

	def clean(self):
		user = authenticate(
			username = self.cleaned_data['email'],
			password = self.cleaned_data['password']
		)

		if user is not None:
			return self.cleaned_data
		raise forms.ValidationError('Invalid Email or Password')

