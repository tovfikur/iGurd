# Generated by Django 3.1 on 2020-08-17 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_loogedin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoogedIn',
            new_name='LoggedIn',
        ),
    ]