from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>Hello World From Si THu PHyo</h1>")