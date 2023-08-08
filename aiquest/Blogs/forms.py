from django import forms

class TeachersRegistration(forms.Form):
    first_name= forms.CharField(label="Enter your first name", label_suffix='')
    last_name = forms.CharField(initial='Uchchhash' )
    email= forms.EmailField(initial="uchchhash@gmail.com", disabled='true')
    password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    Checkbox = forms.CharField(widget=forms.CheckboxInput)