from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from api.models import User, Report
import crypt


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('owner', 'subscribers', 'savedData')


class UserSerializer(serializers.ModelSerializer):
    user_reports = ReportSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'bio', 'friends', 'user_reports')


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
        "input_type": "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        password = make_password(password, hasher='pbkdf2_sha256')
        return User.objects.create(username=username, email=email, password=password)

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', make_password(instance.password, hasher='pbkdf2_sha256'))
        instance.save()
        return instance
