from django.shortcuts import render

# Create your views here.

def annual_athletics(request):
	return render(request,'Athletics/athletic-meet.html', {})

def josh(request):
	return render(request,'Athletics/josh.html', {})

def games(request): 
	return render(request,'Athletics/games.html', {})

def yoga(request): 
	return render(request,'Athletics/yoga.html', {})

def athletics(request): 
	return render(request,'Athletics/athletics.html', {})

