from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings as django_settings
from django.http import HttpResponse
from django.template.context_processors import csrf


def home(request):
	return render(request,'SacMnnit/home.html', {})

def downloads(request): 
	return render(request,'SacMnnit/downloads.html', {})

def president(request): 
	return render(request,'SacMnnit/president.html', {})

def contact(request): 
	return render(request,'SacMnnit/contact.html', {})

def contactmail(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	message = request.POST.get('message')
	subject = request.POST.get('subject')
	to_user = [django_settings.EMAIL_HOST_USER]
	from_user = django_settings.EMAIL_HOST_USER
	send_mail(subject,message,from_user,to_user,fail_silently=False)

	return HttpResponse('success')





