from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import register_user, CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('login/', views.login_user, name="login"),
    # path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    # path('register/', views.register_user, name="register"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('register/', register_user, name="register"),
    path('user/register', CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
]