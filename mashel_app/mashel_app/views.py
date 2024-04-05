from django.shortcuts import HttpResponse,render,redirect
from django.http import JsonResponse

def index(request):
    return render(request,'index.html')

def index(request):
    return render(request,'products.html')