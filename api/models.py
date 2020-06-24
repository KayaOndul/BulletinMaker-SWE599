from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    friends = models.ManyToManyField("self", blank=True)
    username = models.CharField(max_length=30, unique=True, blank=False)
    email = models.CharField(max_length=50, unique=True, blank=False)

    # created_reports=models.ForeignKey('Report',on_delete=models.PROTECT,related_name='created_reports')

    def __str__(self):
        return self.username


class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    subscribers = models.ManyToManyField(
        User,
        through="ReportSubscription",
        related_name='report_members'

    )


class Pane(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='parent_report')
    subscribers = models.ManyToManyField(
        User,
        through='PaneSubscription',
        related_name='pane_members'
    )
    savedData = JSONField(blank=True, null=True)


class PaneSubscription(models.Model):
    pane = models.ForeignKey(Pane, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now=True)


class ReportSubscription(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now=True)
