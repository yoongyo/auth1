from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='{% url travel:main %}'), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^signup/$', views.signup, name="signup")
]