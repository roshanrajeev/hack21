# Generated by Django 3.0.6 on 2020-11-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_is_judge'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
    ]