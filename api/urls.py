from django.urls import path, include

from api import views
from api.views import UserViews

urlpatterns = [
    # path('user/',views.UserViews.index,name="getUser"),
    path('user/',include([
        path('',views.UserViews.getAllUsers,name='users_all'),
        path('<username>',UserViews.getUser,name='get_user')
    ])),

]
