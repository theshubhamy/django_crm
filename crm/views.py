from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sayHello (request):
	return render(request, 'home.html', {'name':"Shubham Kumar", 'age':"23"})