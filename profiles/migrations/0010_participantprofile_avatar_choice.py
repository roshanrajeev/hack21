# Generated by Django 3.0.6 on 2020-11-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_participantprofile_website_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantprofile',
            name='avatar_choice',
            field=models.CharField(default='nota', max_length=25, verbose_name='Which of the following Characters do you relate yourselves to the most?'),
        ),
    ]