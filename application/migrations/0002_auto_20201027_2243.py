# Generated by Django 3.0.6 on 2020-10-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='strength',
        ),
        migrations.AlterField(
            model_name='team',
            name='application_status',
            field=models.CharField(choices=[('Not Submitted', 'Not Submitted'), ('Submitted', 'Submitted'), ('Under Review', 'Under Review'), ('Declined', 'Declined'), ('Waitinglist', 'Waitinglist'), ('Accepted', 'Accepted')], default='Not Submitted', max_length=14),
        ),
    ]
