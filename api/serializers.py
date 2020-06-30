from abc import ABCMeta

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from api.models import User, Report, File



class ReportSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    subscribers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Report
        fields = ('title', 'owner', 'subscribers', 'id', 'layout')


class ReportSerializerEssential(serializers.ModelSerializer):
    subscribers = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Report
        fields = ('title', 'subscribers', 'id', 'owner')


class UserSerializer(serializers.ModelSerializer):
    user_reports = ReportSerializerEssential(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'bio', 'friends', 'user_reports', 'id')

    def __str__(self):
        return self.username


class SearchSerializer(serializers.Serializer):
    users = UserSerializer(many=True)
    reports = ReportSerializerEssential(many=True)


class ProfileSerializer(serializers.Serializer):
    followed_reports = ReportSerializerEssential(many=True)
    authored_reports = ReportSerializerEssential(many=True)
    followed_by = serializers.StringRelatedField(many=True)
    followed_users = serializers.StringRelatedField(many=True)





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


class LikeSerializer(serializers.Serializer):
    model = serializers.CharField(required=True)
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
