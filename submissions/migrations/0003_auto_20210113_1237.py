# Generated by Django 3.0.6 on 2021-01-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_auto_20210111_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='abstract',
            field=models.TextField(max_length=2000),
        ),
    ]
