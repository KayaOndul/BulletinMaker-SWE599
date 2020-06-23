from api.models import *
from api.serializers import *


class UserService:
    def get_user_by_username(self, username):
        user = User.objects.filter(username=username)
        return UserSerializer(user, many=False)

    def get_all_users(self):
        users = User.objects.all()
        return UserSerializer(users, many=True)

    def save_user(self, data):
        if data.password2 is not data.password:
            raise ValueError("Passwords doesn't match")
        elif data.username is None or data.email is None:
            raise ValueError("No username or email provided. Check inputs")

        return User.objects.create(username=data.username,
                                   password=data.password,
                                   email=data.email)

    def change_password(self, data):
        if data.password2 is not data.password:
            raise ValueError("Passwords doesn't match")
        user = User.objects.filter(username=data.username, many=False)
        user.set_password(data.password)
        return UserSerializer(user)
