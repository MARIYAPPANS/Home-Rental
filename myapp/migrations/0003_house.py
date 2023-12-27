# Generated by Django 3.2.13 on 2023-12-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_usermodel_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('cost_of_rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('restrictions', models.TextField()),
                ('bedrooms', models.IntegerField()),
                ('ac_non_ac', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='house_photos/')),
            ],
        ),
    ]
