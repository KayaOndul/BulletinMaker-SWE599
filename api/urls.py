from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views


urlpatterns = [
    path(r'users/<str:username>',views.UserViews.by_username,name='by_usename'),
    path(r'users/<str:username>/changepassword',views.UserViews.change_password,name='change_password'),

]
