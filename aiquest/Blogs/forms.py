from django import forms
from django.core import validators

class TeachersRegistration(forms.Form):
    first_name= forms.CharField(label="Enter your first name", label_suffix='')
    last_name = forms.CharField(initial='Uchchhash' )
    email= forms.EmailField(initial="uchchhash@gmail.com", disabled='true')
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput) 
    Checkbox = forms.CharField(widget=forms.CheckboxInput)
    
    
    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repassword']
        
        if rightpass != wrongpass:
            raise forms.ValidationError('Password does not match')