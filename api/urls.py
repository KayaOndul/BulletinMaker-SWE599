from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api import views
from api.views import FileUploadView

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('api/', include([
        path('register/', views.AuthViews.register, name="register"),
        path('login/', views.AuthViews.login, name="login"),
        path('logout/', views.AuthViews.logout, name="logout"),
        path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        path('users/', include([
            path('', views.UserViews.getAll),
            path(r'<str:username>/', views.UserViews.user),
        ])),
        path('reports/', include([
            path('',views.ReportViews.report_list),
            re_path(r'^(?P<user>.*)/$', views.ReportViews.report_list,name="get_with_params"),
            path('<id>', views.ReportViews.report_detail)
        ])),
        re_path(r'^search/(?P<user>.*)&&(?P<keyword>.*)/$', views.SearchViews.search)

    ]))

]
