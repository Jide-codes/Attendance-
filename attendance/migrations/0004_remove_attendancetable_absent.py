# Generated by Django 4.1.4 on 2022-12-26 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendancetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancetable',
            name='absent',
        ),
    ]
