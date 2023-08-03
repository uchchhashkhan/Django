from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    return HttpResponse('<h1> Welcome to My First Django App </h1>')

def deep_learning(request):
    return HttpResponse('<h1> Deep learning </h1>')

def about_us(request):
    return HttpResponse('<h1> We have availabe experienced Teacher </h1>')
