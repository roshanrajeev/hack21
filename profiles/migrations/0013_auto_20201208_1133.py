# Generated by Django 3.0.6 on 2020-12-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_participantprofile_pin_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantprofile',
            name='website_link',
            field=models.URLField(blank=True, verbose_name='Portfolio Website Link'),
        ),
    ]
