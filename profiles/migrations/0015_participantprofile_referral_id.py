# Generated by Django 3.0.6 on 2020-12-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20201210_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantprofile',
            name='referral_id',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]
