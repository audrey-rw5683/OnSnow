from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

from django.contrib.auth.views import LogoutView

class PatchLogoutView(LogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("logout/", PatchLogoutView.as_view(), name='logout'),
    path("signup/", views.SignUp.as_view(), name='signup'),
]
