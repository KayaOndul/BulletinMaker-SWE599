from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    friends = models.ManyToManyField("self",blank=True)
    username = models.CharField(max_length=30,unique=True,blank=False)
    email=models.CharField(max_length=50,unique=True,blank=False)

    # created_reports=models.ForeignKey('Report',on_delete=models.PROTECT,related_name='created_reports')

    def __str__(self):
        return self.username


class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    subscribers = models.ManyToManyField(
        User,
        through="Subscription",

    ),
    savedData = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
