from django.shortcuts import redirect
from django.http import HttpResponse

# when the user is logged in this should not back to login again

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func

# creating restricted pages

def allowed_users(allowed=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            return view_func()
        return wrapper_func()
    return decorator()


