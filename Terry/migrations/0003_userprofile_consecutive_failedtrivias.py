# Generated by Django 5.1.3 on 2024-12-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Terry', '0002_userprofile_consecutive_trivias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='consecutive_failedtrivias',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]