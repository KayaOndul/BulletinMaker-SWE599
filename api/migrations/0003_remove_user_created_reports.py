# Generated by Django 3.0.7 on 2020-06-23 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200623_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_reports',
        ),
    ]
