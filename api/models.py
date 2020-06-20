from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=60,blank=False)
    password=models.CharField(max_length=256,blank=False)
    email=models.EmailField(max_length=60)

    def __str__(self):
        return self.name
