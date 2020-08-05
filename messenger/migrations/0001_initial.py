# Generated by Django 3.0.8 on 2020-08-03 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('middleware', '0017_auto_20200803_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('Replays', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='messenger.Chat')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='middleware.Transaction')),
            ],
        ),
    ]