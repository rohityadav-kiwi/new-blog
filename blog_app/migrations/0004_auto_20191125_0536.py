# Generated by Django 2.2.7 on 2019-11-25 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20191122_0542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['created_date']},
        ),
    ]
