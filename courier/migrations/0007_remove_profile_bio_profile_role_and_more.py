# Generated by Django 4.0 on 2022-01-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0006_rename_birth_date_profile_birthdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='currentAddress',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='permanentAddress',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
