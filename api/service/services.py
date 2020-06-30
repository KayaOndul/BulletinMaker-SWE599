from api.models import User, Report
from api.serializers import UserSerializer, ReportSerializer


class UserService:

    def get_all_users(self):
        users = User.objects.all()
        return UserSerializer(users, many=True).data


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
