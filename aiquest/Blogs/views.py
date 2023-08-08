from django.http import HttpResponse
from django.shortcuts import render
from . forms import TeachersRegistration

# Create your views here.
def blog1(request):
    return render(request,'blogs/blogs.html')

def showformsdata(request):
    fm=TeachersRegistration()    
    return render(request, 'blogs/forms.html',{'form': fm})