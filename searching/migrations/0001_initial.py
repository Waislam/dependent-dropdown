# Generated by Django 4.0.6 on 2022-08-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=50)),
            ],
        ),
    ]
