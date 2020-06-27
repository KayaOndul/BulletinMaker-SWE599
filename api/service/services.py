from api.models import User, Report
from api.serializers import UserSerializer, ReportSerializer, CreateReportSerializer, PatchReportSerializer


class UserService:
    def get_user_by_username(self, username):
        user = User.objects.filter(username=username)
        return UserSerializer(user, many=False)

    def get_all_users(self):
        users = User.objects.all()
        return UserSerializer(users, many=True).data

    def change_password(self, request):
        pass
        # todo
        # if request.data.password2 is not request.data.password:
        #     raise ValueError("Passwords doesn't match")
        # user = User.objects.filter(username=request.data.username, many=False)
        # user.set_password(request.data.password)
        # return UserSerializer(user)


class ReportService:
    def create_report(self, user):
        report = Report.objects.create(owner=user)
        return CreateReportSerializer(report, many=False)

    def patch_report(self, id):
        Report.objects.filter(id=id).update(layout=self['layout'], title=self['title'])
        return Report.objects.get(id=id)

    def get_reports(self, user):
        pass
        # reports = Report.objects.filter(owner=user)
        # return ReportSerializer(reports, many=True)
