from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from api import views

router = routers.DefaultRouter()
router.register(r'Person', views.PersonViewSet)

urlpatterns = [
    path('user/',views.),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
