# Generated by Django 3.1.2 on 2021-01-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignment',
            name='dest',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='consignment',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='consignment',
            name='pincode',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
