# Generated by Django 4.2.4 on 2023-08-28 11:35

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=30)),
                ('stu_city', models.CharField(max_length=30)),
            ],
            managers=[
                ('student', django.db.models.manager.Manager()),
            ],
        ),
    ]
