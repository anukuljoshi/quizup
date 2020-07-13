from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import get_user_model, authenticate, views as auth_views

from .forms import RegistrationForm, LoginForm

User = get_user_model()


def register_view(request, *args, **kwargs):
    form = RegistrationForm()
    if(request.POST):
        form = RegistrationForm(data=request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)
            
            return redirect(reverse('login'))
        else:
            context = {
                'form' : form,
                'errors' : form.errors
            }
            print(form.errors)
            return render(request, 'users/registration.html', context)
    context = {
        'form' : form
    }
    return render(request, 'users/registration.html', context)

# def login_view(request, *args, **kwargs):
#     form = LoginForm()
#     if(request.POST):
#         form = LoginForm(request.POST)
#         if(form.is_valid()):
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             user = authenticate(User, username=username, password=password)
#             if(user):
#                 print(user)
#             else:
#                 print('failed')
#             redirect(reverse('home'))
    
#     context = {
#         'form' : form
#     }
#     return render(request, 'users/login.html', context)


def logout_view(request, *args, **kwargs):
    return auth_views.logout_then_login(request, login_url=reverse('login'))
    

def user_detail_view(request, uname,*args, **kwargs):
    qs = get_object_or_404(User, username=uname)
    # qs = User.objects.get(username=uname)
    context = {
        'username' : uname,
        'object' : qs
    }

    return render(request, 'users/user-profile.html', context)

