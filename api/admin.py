from django.contrib import admin
from .models import User, Report, Pane, ReportSubscription, PaneSubscription

# Register your models here.

admin.site.register(User)
admin.site.register(Report)
admin.site.register(PaneSubscription)
admin.site.register(ReportSubscription)
admin.site.register(Pane)
