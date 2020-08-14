# Generated by Django 3.1 on 2020-08-14 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.TextField(blank=True, null=True)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('Seen', models.BooleanField(default=False)),
                ('UserID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='user.userdetails')),
            ],
        ),
    ]
