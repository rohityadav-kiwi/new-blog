# Generated by Django 2.2.7 on 2019-11-25 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20191125_0536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
