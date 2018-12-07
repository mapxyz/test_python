from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def auth(request):
    msg = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:

                if user.is_active:
                    login(request, user)
                    msg = "User is valid, active and authenticated"

                    return HttpResponseRedirect('/')
                else:
                    msg = "The password is valid, but the account has been disabled!"
            else:
                msg = "Login or Passwrod Wrong"
        return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'loginForm': form, 'msg': msg})




