from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        return self.name


class Report(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(
        User,
        through="Subscription",

    )

    def __str__(self):
        return self.name


class Subscription(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
