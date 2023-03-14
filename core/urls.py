from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LogoutView
from .forms import LoginForm
app_name = 'core'

urlpatterns =[
    path('', views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('', auth_views.LogoutView.as_view(template_name='core/index.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login')
]