# Generated by Django 3.0.6 on 2020-11-18 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_organizer',
            field=models.BooleanField(default=False),
        ),
    ]