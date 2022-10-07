# Generated by Django 4.1 on 2022-08-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('STUDENTS', 'Student'), ('TEACHER', 'Teacher')], default=('ADMIN', 'Admin'), max_length=20),
        ),
    ]