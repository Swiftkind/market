from django.shortcuts import render
from django.views.generic import (TemplateView,View)
from .models import User
from django.http import JsonResponse
from django.shortcuts import render,render_to_response
from django.template.loader import render_to_string
from django.contrib.auth import (authenticate,login)
from django.http import HttpResponse
from django.template import RequestContext
from .forms import (RegisterForm,LoginForm)
import simplejson	


class Home(TemplateView):
	"""
	home
	"""

	template_name = 'home/home.html'


	def get(self,request,*args,**kwargs):

		context = {
			'log_forms': LoginForm()
		}
		
		return render(request,self.template_name,context)


class Register(TemplateView):
	"""
	register
	"""

	template_name = 'account/register.html'
	
	context = {
			'forms': RegisterForm(),
			'log_forms': LoginForm(),
		}

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,self.context)

	def post(self,request,*args,**kwargs):

		form = RegisterForm(request.POST)

		if form.is_valid():
			user = User.objects.create_user(
				form.cleaned_data['email'],	
				form.cleaned_data['password'],	
			)

			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.save()
			
			login(request,user)

			context = {
				'user': request.user,
			}

			return render(request,'home/home.html',context)

		return JsonResponse(form.errors,safe=False)


		

class Login(TemplateView):
	"""
	login
	"""
	template_name = 'account/register.html'

	context = {
		'forms': RegisterForm(),
		'log_forms': LoginForm(),
	}

	def post(self,request,*args,**kwargs):
		form = LoginForm(request.POST)

		if form.is_valid():
			user = authenticate(
				username=form.cleaned_data['email'],
				password=form.cleaned_data['password']
			)

			login(request,user) 

			context = {
				'log_forms': LoginForm(),
				'user': request.user,
			}
	
			return render(request,'home/home.html', context)

		return JsonResponse(form.errors,safe=False)

			
