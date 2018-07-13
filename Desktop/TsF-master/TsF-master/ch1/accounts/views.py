from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm

# from .forms import LoginForm
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers



@login_required
def profile(request):
    request.user
    return render(request, 'accounts/profile.html')

signup = CreateView.as_view(model=User, form_class=SignupForm, success_url=settings.LOGIN_URL, template_name='accounts/signup.html')


"""
def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
        else:
            form = SignupForm()
        return render(request, 'accounts/signup_form.html',{
            'form':form,
        })

def profile(request):
    return render(request, 'accounts/profile.html')



def login(request):
    providers = []
    for provider in get_providers():     # settings/INSTALLED_APPS 내에서 활성화된 목록
        # social_app속성은 provider에는 없는 속성입니다.
        try:
            # 실제 Provider 별 Client id/secret 이 등록이 되어있는가?
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
        authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})
"""
