# Generated by Django 3.2.9 on 2021-12-30 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_student_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='marks',
        ),
    ]