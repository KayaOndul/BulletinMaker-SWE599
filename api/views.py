from django.contrib.auth import logout, authenticate
from django.http import JsonResponse
from rest_framework import status, permissions, response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Report
from api.serializers import UserSerializer, UserCreateSerializer, CreateReportSerializer, \
    FileSerializer, PatchReportSerializer
from api.service.services import UserService, ReportService


class UserViews:

    @api_view(["GET", "PATCH"])
    def user(self, request, username):
        if request.method is "GET":
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            data = UserService.get_user_by_username(username)
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        if request.method is "PATCH":
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
            data = JSONParser().parse(self)
            serializer = PatchReportSerializer(report, data=data)
            if serializer.is_valid():
                report = ReportService.patch_report(data, id)
                if serializer.is_valid():
                    return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED, safe=False)
                else:
                    return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
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

    @api_view(['GET', "POST"])
    def report_list(self):
        if self.method == "POST":

            serializer = CreateReportSerializer(data=self.data)

            report = ReportService.create_report(serializer, user=self.user)
            return JsonResponse(report.data, status=status.HTTP_201_CREATED, safe=False)
        else:
            pass
            # serializer = ReportSerializer(data=self.data)
            # user = User.objects.get(username=username)
            # reports = ReportService.get_reports(serializer, user=user)
            # return JsonResponse(reports.data, status=status.HTTP_200_OK, safe=False)


class SearchViews:
    @api_view(['GET', ])
    def search(self, user, keyword):
        print(user, keyword)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
