from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
