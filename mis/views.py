from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_cpu_info(request):
    return HttpResponse("success")

def get_tce_package(request):
    pass