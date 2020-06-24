from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api import views

urlpatterns = [
    path('api/', include([
        path('register', views.AuthViews.register, name="register"),
        path('login', views.AuthViews.login, name="login"),
        path('logout', views.AuthViews.logout, name="logout"),
        path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("refresh", TokenRefreshView.as_view(), name="token_refresh"),
        path('users/', include([
            path('', views.UserViews.getAll),
            path(r'<str:username>/', include([
                path('', views.UserViews.user),
                path('reports/', include([
                    path('', views.ReportViews.report_list),
                    path('<id>', views.ReportViews.report_detail)
                ])),
                path('subscriptions/', include([
                    path('', views.SubscriptionViews.subscription_list),
                    path('<id>', views.SubscriptionViews.subscription_detail)
                ]))
            ])),

        ]))
    ]))

]
