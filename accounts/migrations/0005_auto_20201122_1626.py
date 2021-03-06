# Generated by Django 3.0.6 on 2020-11-22 10:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='slug',
        ),
        migrations.AddField(
            model_name='account',
            name='urlid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
