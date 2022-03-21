from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as user_views


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', user_views.SignUp.as_view(), name='signup'),
    path('profile/', user_views.profile, name='profile'),
]