from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
# from .views import CreateUserView, RegisterView, ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    # path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('register', RegisterView.as_view(), name="register"),
    # path('user/create', CreateUserView.as_view(), name="create_user"),
    # path("token/", TokenObtainPairView.as_view(), name="get_token"),
    # path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    # path("api-auth/", include("rest_framework.urls")),
    # path('protected/', ProtectedView.as_view(), name='protected'),
]