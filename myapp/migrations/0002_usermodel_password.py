# Generated by Django 3.2.13 on 2023-12-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default='123', max_length=255),
        ),
    ]