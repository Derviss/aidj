# Generated by Django 3.2.7 on 2022-03-17 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='deep_link',
        ),
    ]
