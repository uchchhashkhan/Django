from django.http import HttpResponse
from django.shortcuts import render
from . forms import TeachersRegistration

# Create your views here.
def blog1(request):
    return render(request,'blogs/blogs.html')

def showformsdata(request):
    if request.method == 'POST':
        fm=TeachersRegistration(request.POST)
        if fm.is_valid():
         print(fm.cleaned_data['password'])
         print(fm.cleaned_data['repassword'])
    fm=TeachersRegistration()    
    print('This is get statement')
    return render(request, 'blogs/forms.html',{'form': fm})