from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Team(AbstractUser):

    Registered_StartUp = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        )

    Sectors = (
                  ('Health', 'Health'),
                  ('Women Empowerment', 'Women Empowerment'),
                  ('Pollution', 'Pollution'),
                  ('Education', 'Education'),
                  ('Employability', 'Employability'),
                  ('Agriculture and Farming', 'Agriculture and Farming'),
                  ('5R-Reuse, Reduce,Recycle,Recover,Refuse', '5R-Reuse, Reduce,Recycle,Recover,Refuse'),
                  ('Sustainable Energy', ' Sustainable Energy'),
                  ('Financial Inclusion and Fintech', 'Financial Inclusion and Fintech'),
                  ('Water management', 'Water management'),
                  ('Security', 'Security'),
                  ('Rural development', 'Rural development'),
    )

    team_name                       = models.CharField(max_length=100)
    team_leader_name                = models.CharField(max_length=100)
    team_leader_emailID             = models.EmailField(max_length=100, blank=False, unique=True)
    team_leader_phone_number        = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number_alternate          = PhoneNumberField(null=False, blank=False, unique=True)
    name_of_organisation            = models.CharField(max_length=200, blank=True, null=True)
    is_startup                      = models.CharField(choices=Registered_StartUp, max_length=20)
    city_name                       = models.CharField(max_length=100)
    team_member2_name               = models.CharField(max_length=100)
    team_member3_name               = models.CharField(max_length=100, blank=True, null=True)
    team_member4_name               = models.CharField(max_length=100, blank=True, null=True)
    team_member5_name               = models.CharField(max_length=100, blank=True, null=True)
    team_member6_name               = models.CharField(max_length=100, blank=True, null=True)
    team_member7_name               = models.CharField(max_length=100, blank=True, null=True)
    team_member8_name               = models.CharField(max_length=100, blank=True, null=True)
    sectors_selection               = models.CharField(choices=Sectors, max_length=200)
    alternate_member_details_name   = models.CharField(max_length=100)
    alternate_member_details_email  = models.EmailField(max_length=100)
    referral_code                   = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username
