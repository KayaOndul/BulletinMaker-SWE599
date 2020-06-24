from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api import views

urlpatterns = [
    path('register/', views.AuthViews.register, name="register"),
    path('login/', views.AuthViews.login, name="login"),
    path('logout/', views.AuthViews.logout, name="logout"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(r'users/', include([
        path('', views.UserViews.getAll),
        path(r'<str:username>', views.UserViews.getUser),

    ]))
]
