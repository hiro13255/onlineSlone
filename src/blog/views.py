from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print("Hello")
    return HttpResponse("<h1>Hello</h1>")