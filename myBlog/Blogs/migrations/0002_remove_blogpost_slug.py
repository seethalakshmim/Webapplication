# Generated by Django 3.2.6 on 2021-08-06 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
    ]
