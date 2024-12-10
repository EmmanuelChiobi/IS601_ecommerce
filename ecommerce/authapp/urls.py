from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import register_user

urlpatterns = [
    # path('login/', views.login_user, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    # path('register/', views.register_user, name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', register_user, name="register"),
]