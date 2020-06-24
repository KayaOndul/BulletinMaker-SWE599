from api.models import User
from api.serializers import UserSerializer


class UserService:
    def get_user_by_username(self, username):
        user = User.objects.filter(username=username)
        return UserSerializer(user, many=False)

    def get_all_users(self):
        users = User.objects.all()
        return UserSerializer(users, many=True).data

    def change_password(self, request):
        if request.data.password2 is not request.data.password:
            raise ValueError("Passwords doesn't match")
        user = User.objects.filter(username=request.data.username, many=False)
        user.set_password(request.data.password)
        return UserSerializer(user)

