from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from api.models import Report
from api.serializers import ReportSerializer
from api.services import UserService


class UserViews:

    @api_view(["GET", "POST"])
    def by_username(self, request, username, body):
        if request is "GET":
            data = UserService.get_user_by_username(username)
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        elif request is "POST":
            data = UserService.save_user(body)
            return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)

    @api_view(["PUT"])
    def change_password(self, data):
        data = UserService.change_password(data)
        return JsonResponse(data, safe=False, status=status.HTTP_202_ACCEPTED)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
