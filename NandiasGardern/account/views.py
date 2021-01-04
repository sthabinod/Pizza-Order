from pyexpat.errors import messages

from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
# how to register when we have own custom user


@unauthenticated_user
def login_user(request):
    message = ""
    if request.method == 'POST':
        u= request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(request,username=u,password=pw)
        if user:
            login(request,user)
            return redirect('index')
        else:
            message = "Please enter correct username or password"

    return render(request, 'account/login.html',{'message':message})


@unauthenticated_user
def register(request):
    # message= 'Not registerd yet'
    # form = CustomUserForm()
    # message = 'form has been sent'
    # if request.method == 'POST':
    #     message = "Post has been accepted"
    # #     # form data are passed here
    #     form= CustomUserForm(request.POST)
    #     message = "Form accepeted"
    #     if form.is_valid():
    #         form.save()
    #         print("Successfully created")
    #
    # #         user = form_filled.save()
    # #         group = Group.objects.get(name='customer')
    # #         user.groups.add(group)
    #         message = 'You are registered successfully.'
    #         return redirect('login')
    # return render(request, 'account/register.html',{'form':form,'message':message})
    # #
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            # messages.success(request, 'Account created successfully')
            print("Successfully created")
            return redirect('login')
        else:
            print("Error")

    context = {'form': form}
    return render(request, "account/register.html", context)


def logout_user(request):
    logout(request)
    return redirect('index')

