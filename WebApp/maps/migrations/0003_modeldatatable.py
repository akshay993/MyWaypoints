# Generated by Django 2.1.1 on 2018-10-05 19:08

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_datatable'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelDataTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start', models.CharField(max_length=200)),
                ('End', models.CharField(max_length=200)),
                ('Mode', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('google_response', django_mysql.models.JSONField(default=dict)),
                ('weather_response', models.TextField(max_length=1000)),
            ],
        ),
    ]
