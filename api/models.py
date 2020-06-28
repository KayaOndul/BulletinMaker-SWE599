from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    friends = models.ManyToManyField("self", blank=True)
    username = models.CharField(max_length=30, unique=True, blank=False)
    email = models.CharField(max_length=50, unique=True, blank=False)

    def __str__(self):
        return self.username


class Report(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    layout = JSONField(blank=True, null=True)
    subscribers = models.ManyToManyField(User, null=True)

    def __str__(self):
        return self.title


class ReportSubscription(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.report.title + ' / ' + self.person.username


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
