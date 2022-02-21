from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from Custom_model.models import CreateUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Custom_model.forms import CreatUserForm, LoginForm


# Create your views here.
def signup(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Custom_model:login'))
    diction = {'form': form}
    return render(request, 'Custom_model/signup.html', context=diction)


def login_user(request):
   form = LoginForm(request.POST or None)
   if request.method == 'POST':
      if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return HttpResponseRedirect(reverse('Custom_model:staff'))
        elif user is not None and user.is_employee:
            login(request, user)
            return HttpResponseRedirect(reverse('Custom_model:employee'))
   return render(request, 'Custom_model/login.html', context={'form': form})


    # form = AuthenticationForm()
    # if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(email=email, password=password)
    #         if user is not None and user.is_staff:
    #             login(request, user)
    #             return HttpResponseRedirect(reverse('Custom_model:index'))
    #
    #         elif user is not None and user.is_employee:
    #             login(request, user)
    #             return HttpResponseRedirect(reverse('Custom_model:index'))
    # diction = {'form': form}
    # return render(request, 'Custom_model/login.html', context=diction)
    #

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Custom_model:login'))

def index(request):
    return render(request, 'Custom_model/home.html', context={})

def Employee(request):
    return render(request, 'Custom_model/employee.html', context={})

def Staff(request):
    return render(request, 'Custom_model/staff.html', context={})