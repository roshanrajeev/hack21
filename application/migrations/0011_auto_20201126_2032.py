# Generated by Django 3.0.6 on 2020-11-26 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20201111_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='received_confirmation_mail',
            field=models.BooleanField(default=False),
        ),
    ]
