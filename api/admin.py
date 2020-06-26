from django.contrib import admin

from .models import User, Report, Pane, ReportSubscription

# Register your models here.

admin.site.register(User)
admin.site.register(Report)
admin.site.register(ReportSubscription)
admin.site.register(Pane)
