# Generated by Django 4.0.1 on 2022-01-06 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0012_profile_firstname_profile_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastName',
        ),
    ]