from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from user.models import CustomUser
from accounts.models import Account
from .choices import *
# Create your models here.

class ParticipantProfile(models.Model):
    user = models.OneToOneField(Account, related_name='profile', on_delete=models.CASCADE)

    team_status = models.CharField(max_length=10, choices=TEAM_STATUS_CHOICES, default='Has Team', blank=False)
    name = models.CharField(max_length=256, blank=False)
    contact = models.CharField(max_length=13, blank=False)
    dob = models.DateField()
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES, blank=False)
    bio = models.TextField()
    projects = models.TextField(blank=False, default='')
    tshirt_size = models.CharField(max_length=3, choices=T_SHIRT_SIZE_CHOICES, verbose_name='T-Shirt Size')
    #emergency conatct
    skills = models.TextField()
    educational_institution = models.CharField(max_length= 128)
    field_of_study = models.CharField(max_length=30, choices=FIELD_OF_STUDY_CHOICES, blank=False, default='Engineering', verbose_name='Field of Study')
    is_ieee = models.IntegerField(choices=BOOLEAN_CHOICES, default=0, blank=False, verbose_name="Are you an IEEE member?")
    shipping_address = models.TextField(blank=False, default=' ')
    pin_code = models.CharField(blank=False, default='', max_length=10, )
    state = models.CharField(max_length=41, choices=STATE_OF_RESIDENCE_CHOICES, blank=False, default='Kerala', verbose_name='State/Province of Residence')
    educational_status = models.CharField(max_length=12, blank=False, choices=EDUCATIONAL_STATUS_CHOICES, default='Bachelors')
    year_of_graduation = models.IntegerField(choices=YEAR_OF_GRADUATION_CHOICES, blank=False, default=2023)
    # previous_projects
    website_link = models.URLField(verbose_name="Portfolio Website Link", blank=True)
    github_profile_link = models.URLField(verbose_name="GitHub Profile Link", blank=True)
    twitter_profile_link = models.URLField(verbose_name="Twitter Profile Link", blank=True)
    linkedin_profile_link = models.URLField(verbose_name="LinkedIn Profile Link", blank=True)
    avatar_choice = models.CharField(max_length=25, blank=False, default="nota", verbose_name="Which of the following Characters do you relate yourselves to the most?")
    referral_id = models.CharField(max_length=7, blank=True)
    
    welcome_mail_sent = models.BooleanField(default=False)
    # resume_link = models.URLField(verbose_name="Link to your resume", blank=True)

    def __str__(self):
        return self.user.email

# @receiver(post_save, sender=Account)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         ParticipantProfile.objects.create(user=instance)
#     instance.ParticipantProfile.save()


# class VolunteerProfile(models.Model):
#     user = models.OneToOneField(Account, on_delete=models.CASCADE)
#     batch = models.CharField(max_length=4, blank=False, default=' ', choices=CLASS_CHOICES)
#     name = models.CharField(max_length=256, blank=False)
#     email = models.EmailField(max_length=256, blank=False, unique=True)
#     contact = models.IntegerField( blank=False)
#     dob = models.DateField()
#     gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=False)
#     tshirt_size = models.CharField(max_length=3, choices=T_SHIRT_SIZE_CHOICES, verbose_name='T-Shirt Size')

# class OrganizerProfile(moels.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     batch = models.CharField(max_length=4, blank=False, default=' ', choices=CLASS_CHOICES)
#     name = models.CharField(max_length=256, blank=False)
#     contact = models.IntegerField( blank=False)
#     dob = models.DateField()
#     gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=False)