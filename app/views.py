from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def dangky(request):
    return render(request, 'app/dangky.html')

def dangnhap(request):
    return render(request, 'app/dangnhap.html')

def danhsachnhac(request):
    return render(request, 'app/danhsachnhac.html')

def thuvien(request):
    return render(request, 'app/thuvien.html')

