from django.shortcuts import render

# Create your views here.

def culrav(request):
	return render(request,'Culural/culrav.html', {})
	
def eloquence(request):
	return render(request,'Cultural/eloquence.html', {})
	
def literary(request):
	return render(request,'Cultural/literary.html', {})
	
def cultural(request):
	return render(request,'Cultural/cultural.html', {})
	
def classical(request): 
	return render(request,'Cultural/classical.html', {})