from django import forms
from django.core import validators
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

#custome validation
def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("Name Needs to start with Z")

class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])#custom validators
    email=forms.EmailField()
    verify_email = forms.EmailField(label="Enter Your Email Again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    validators=[validators.MaxLengthValidator(0)]) #in-built validators

    def clean(self):
        all_clean_data = super().clean() #clean data on forms
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure that the emails MATCH!")

'''
    #validation

    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
'''
