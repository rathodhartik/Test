# Generated by Django 3.2.9 on 2021-12-30 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
    ]
