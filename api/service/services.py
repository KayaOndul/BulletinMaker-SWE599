from api.models import User, Report
from api.serializers import UserSerializer, ReportSerializer, CreateReportSerializer, PatchReportSerializer


class UserService:


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
        return ReportSerializer(report, many=False)

    def patch_report(self, id):
        if self.data['title'] is '':
            Report.objects.filter(id=id).update(layout=self.data['layout'])
        else:
            Report.objects.filter(id=id).update(layout=self.data['layout'], title=self.data['title'])
        return Report.objects.get(id=id)


