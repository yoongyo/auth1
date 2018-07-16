from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm

# 로그인 안된 상황에서는 로그인 창이뜨도록 설정
@login_required     # settings.LOGIN_URL
def profile(request):
    request.user    # django.contrib.auth.models.AnonymousUser
    return render(request, 'accounts/profile.html')

"""
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{
        'form':form,
    })
"""

signup = CreateView.as_view(model=User, form_class=SignupForm, success_url=settings.LOGIN_URL, template_name='accounts/signup.html')