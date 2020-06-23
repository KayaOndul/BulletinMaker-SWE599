from rest_framework.decorators import api_view

from .models import User
from rest_framework import viewsets
from .serializers import PersonSerializer


class UserViews:
    @api_view(["GET"])
    def index(request):
