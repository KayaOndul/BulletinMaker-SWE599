from rest_framework import serializers

from api.models import User, Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('owner', 'subscribers', 'savedData')


class UserSerializer(serializers.ModelSerializer):
    user_reports = ReportSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'bio',  'friends','user_reports')
