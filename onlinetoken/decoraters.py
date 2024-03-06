from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home')
            else:
                return view_func(request, *args, **kwargs)
    
    return wrapper_func

def doctor_required(view_func):
    @login_required
    def wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Doctor').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('access_denied')  # Redirect to a page indicating access denied
    return wrapped_view

# def admin_required(view_func):
#     @login_required
#     def wrapped_view(request, *args, **kwargs):
#         if request.user.groups.filter(name='Admin').exists():
#             return view_func(request, *args, **kwargs)
#         else:
#             return HttpResponse('access_denied')  # Redirect to a page indicating access denied
#     return wrapped_view