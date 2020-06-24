from django.contrib.auth import logout, authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import viewsets, status, permissions, response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Report
from api.serializers import ReportSerializer, UserSerializer, UserCreateSerializer
from api.service.services import UserService


class UserViews:

    @api_view(["GET"])
    def getUser(self, request, username):

        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = UserService.get_user_by_username(username)
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    @api_view(["GET"])
    def getAll(self):

        data = list(UserService.get_all_users(self))
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    @api_view(["POST"])
    def addUser(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = UserService.save_user(request.data)
        return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)

    @api_view(["PATCH"])
    def change_password(self, request):
        data = UserService.change_password(request.data)
        return JsonResponse(data, safe=False, status=status.HTTP_202_ACCEPTED)


class AuthViews:
    @api_view(["POST"])
    @permission_classes([permissions.AllowAny])
    def register(request):
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
        }
        return response.Response(res, status.HTTP_201_CREATED)

    @api_view(["POST"])
    @permission_classes([permissions.AllowAny])
    def login(request):
        if request.method == 'POST':
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                res = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "username": user.username
                }
                return response.Response(res, status.HTTP_200_OK)
            else:
                res = {
                    'error': 'User authentication failed!'
                }
                return response.Response(res, status.HTTP_403_FORBIDDEN)

    @api_view(["POST"])
    @permission_classes([permissions.AllowAny])
    def logout(request):
        if request.method == 'POST':
            logout(request)
            return response.Response(None, status.HTTP_204_NO_CONTENT)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
