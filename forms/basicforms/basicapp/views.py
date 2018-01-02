from django.shortcuts import render
from . import forms
from basicapp.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context_dict = {'text': 'hello world','number':100}
    return render(request, 'basicapp/index.html',context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'basicapp/registration.html',
    {'user_form': user_form,
    'profile_form': profile_form,
    'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failde!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED!")
    else:
        return render(request,'basicapp/login.html',{})

def form_name_view(request):
    form=forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'basicapp/form_page.html',{'form':form})

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relative_url_templates.html')
