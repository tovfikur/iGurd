# Generated by Django 3.1 on 2020-08-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('middleware', '0005_auto_20200814_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiontrash',
            name='FixedCash',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
