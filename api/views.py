from django.http import JsonResponse
from rest_framework.decorators import api_view


class UserViews:
    @api_view(["GET"])
    def index(self, request):
        return JsonResponse('Hello', safe=False)

    @api_view(["POST"])
    def postNewUser(self, request):
        pass

    @api_view(["GET"])
    def getAllUsers(self,request):
        pass
