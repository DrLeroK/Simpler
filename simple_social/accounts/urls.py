from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # Redirects to LOGIN_REDIRECT_URL (in settings) on success
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Redirects to LOGOUT_REDIRECT_URL (in settings)
]
