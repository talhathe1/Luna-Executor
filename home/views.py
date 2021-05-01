from django.shortcuts import render
from home.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required



def index(request):
    context_dic = {'name':'mera nam jo bhi ap apne kaam sde', 'age':'31'}
    return render(request, 'home/index.html',context=context_dic)

def base(request):
    return render(request, 'home/base.html')


@login_required
def special(request):
    return HttpResponse('you are logged in nice')


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
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'home/registration.html',
                                                    {'user_form':user_form,
                                                    'registered':registered,
                                                    'profile_form':profile_form})
        


#All the information related to login is here

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                print("account not active")

        else:
            Print("Invalid username and password")
            print("Username: {} Password: {}".format(username,password))
            return HttpResponse("invalid login details")

    else:
        return render(request, "home/login.html",{})
                



# Create your views here.
def others(request):
    return render(request, 'home/others.html')