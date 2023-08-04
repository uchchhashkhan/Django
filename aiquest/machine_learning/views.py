from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def machine_learning(request):
    #course = "Machine Learning"
    #Tclass = 21
    #seat = 20
    #cduration = '2.5 months'
    #offering = {'c' : course, 'tl' : Tclass, 'st' :seat, 'cd' : cduration}  #here, 'offering is a dictionary
    Teachers = {'names':['uchchhash','shamsur','khan']}
    return render(request,'machine_learning/machine_learning.html', context=Teachers)

def random(request):
    return render(request,'machine_learning/random_forest.html')

def k_nearest(request):
    return render(request,'machine_learning/knn.html')

def dtree(request):
    return render(request,'machine_learning/DT.html')
