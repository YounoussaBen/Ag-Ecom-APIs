from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserView
from django.urls import path


urlpatterns = [
    path("user/register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
]