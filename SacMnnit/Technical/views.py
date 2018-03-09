from django.shortcuts import render

# Create your views here.

def avishkar(request):
	return render(request,'Technical/avishkar.html', {})
	
def technological(request):
	return render(request,'Technical/technological.html', {})