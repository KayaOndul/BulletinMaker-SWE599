import json
from itertools import chain

from django.contrib.auth import logout, authenticate
from django.http import JsonResponse
from rest_framework import status, permissions, response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Report, User
from api.serializers import UserSerializer, UserCreateSerializer, CreateReportSerializer, \
    FileSerializer, PatchReportSerializer, ReportSerializer, UserSerializerForSubsciberList, SearchSerializer, \
    LikeSerializer
from api.service.services import UserService, ReportService


class UserViews:

    @api_view(["GET", "PATCH"])
    def user(self, username):
        if self.method == "GET":
            serializer = UserSerializer(data=self.data)

            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        if self.method == "PATCH":
            pass

    @api_view(["GET"])
    def getAll(self):

        data = list(UserService.get_all_users(self))
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)


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
    def logout(self, request):
        if request.method == 'POST':
            logout(request)
            return response.Response(None, status.HTTP_204_NO_CONTENT)


class ReportViews:

    @api_view(["GET", "PATCH", "DELETE"])
    @permission_classes([AllowAny])
    def report_detail(self, id):
        try:
            report = Report.objects.get(id=id)
        except Report.DoesNotExist as e:
            return response.Response({"error": e.args[0]}, status.HTTP_400_BAD_REQUEST)
        if self.method == "PATCH":
            if report.owner.username != self.user.username:
                res = {
                    "error": "Only owner of the report can patch it"
                }
                return response.Response(res, status.HTTP_406_NOT_ACCEPTABLE)

            Report.objects.filter(id=id).update(layout=self.data['layout'], title=self.data['title'])
            report = Report.objects.get(id=id)
            serializer = ReportSerializer(report)
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED, safe=False)
        if self.method == "GET":

            serializer = PatchReportSerializer(report)
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED, safe=False)

        elif self.method == "DELETE":
            if report.owner.username != self.user.username:
                res = {
                    "error": "Only owner of the report can patch it"
                }
                return response.Response(res, status.HTTP_406_NOT_ACCEPTABLE)
            report.delete()
            return response.Response({"detail": 'deleted'}, status.HTTP_200_OK)

    @api_view(["POST"])
    def create_report(self):
        if self.method == "POST":
            serializer = ReportSerializer(data=self.data)

            report = ReportService.create_report(serializer, user=self.user)
            return JsonResponse(report.data, status=status.HTTP_201_CREATED, safe=False)

    @api_view(["GET"])
    @permission_classes([AllowAny])
    def get_reports(self):
        user = self.user
        reports = []
        if user.username == '':
            reports = Report.objects.filter(layout__isnull=False)
        else:
            reports = Report.objects.exclude(owner=user).filter(layout__isnull=False)
        serializer = ReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    @api_view(["GET"])
    @permission_classes([AllowAny])
    def report_list_via_username(self, user):
        key = User.objects.get(username=user)
        reports = Report.objects.filter(owner=key, layout__isnull=False)
        serializer = ReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    @api_view(["GET"])
    @permission_classes([AllowAny])
    def get_subscriptions_via_username(self, user):
        reports = Report.objects.filter(subscribers__username=user)
        serializer = ReportSerializer(reports, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


class SearchViews(RetrieveAPIView):
    @api_view(['POST', ])
    @permission_classes([AllowAny])
    def search(self):
        keyword = self.data['keyword']
        users = User.objects.filter(username__icontains=keyword)
        reports = Report.objects.filter(title__icontains=keyword)
        data = {'users': users, 'reports': reports}
        serializer = SearchSerializer(data)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeViews:
    @api_view(["POST"])
    def like_detail(self):
        user = self.user
        serializer = LikeSerializer(data=self.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.data['model'] == 'report':
            report = Report.objects.get(id=serializer.data['id'])
            if user in report.subscribers:
                report.subscribers.remove(user)
            else:
                report.subscribers.add(user)
        elif serializer.data['model'] == 'user':
            friended_user = User.objects.get(username=serializer.data['name'])
            if User.objects.filter(friends__username__contains=friended_user.username):
                self.user.friends.remove(friended_user)
                res = {'detail': 'Removed ' + friended_user.username + ' from followed users'}
                return response.Response(res, status=status.HTTP_200_OK)
            else:
                self.user.friends.add(friended_user)
                res = {'detail': 'Added ' + friended_user.username + ' to followed users'}
                return response.Response(res, status=status.HTTP_200_OK)
