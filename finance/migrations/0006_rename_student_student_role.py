# Generated by Django 4.1 on 2022-09-07 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_role_student_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student',
            new_name='role',
        ),
    ]