# Generated by Django 3.0.6 on 2021-01-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_auto_20210113_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='problem_statement',
            field=models.CharField(choices=[('Good Health and Well-being', 'Good Health and Well-being'), ('Quality Education', 'Quality Education'), ('Industry, Innovation and Infrastructure', 'Industry, Innovation and Infrastructure'), ('Life on Land', 'Life on Land'), ('Affordable and Clean Energy', 'Affordable and Clean Energy'), ('Agriculture & Rural Development', 'Sustainable Cities and Communities')], max_length=40),
        ),
    ]
