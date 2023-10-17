from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.users.groups.exists():
                group = request.users.groups.all()[0].name

            if request in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("Usuario no autorizado para visitar este sitio")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.users.groups.exists():
                group = request.users.groups.all()[0].name

            if group == 'clientes':
                return redirect('index')

            if group == 'admin':    
                return view_func(request,*args,**kwargs)

        return wrapper_func
    return decorator
