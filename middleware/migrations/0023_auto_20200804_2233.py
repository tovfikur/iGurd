# Generated by Django 3.0.8 on 2020-08-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('middleware', '0022_auto_20200804_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Image4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Image5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='token',
            field=models.CharField(default='9', max_length=200),
        ),
    ]
