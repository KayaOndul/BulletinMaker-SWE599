from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view



# class UserViews:
#     @api_view(["GET"])
#     def getUser(self, request, username):
#         return JsonResponse('Hello ' + username, safe=False)
#
#     @api_view(["POST"])
#     def postNewUser(self, request):
#         pass
#
#     @api_view(["GET"])
#     def getAllUsers(self, request):
#         pass
from api.models import User
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
