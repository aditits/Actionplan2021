from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy

class Team(AbstractUser):
    Registered_StartUp = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        )

    Internet_Connectivity = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    team_name                = models.CharField(max_length=100)
    team_leader_name         = models.CharField(max_length=100)
    team_leader_emailID       = models.EmailField(max_length=100, blank=False, unique=True)
    team_leader_phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number_alternate   = PhoneNumberField(null=False, blank=False, unique=True)
    college_name             = models.CharField(max_length=200)
    is_startup               = models.CharField(choices=Registered_StartUp, max_length=20)
    city_name                = models.CharField(max_length=100)
    team_member2_name        = models.CharField(max_length=100)
    team_member3_name        = models.CharField(max_length=100)
    team_member4_name        = models.CharField(max_length=100)
    team_member5_name        = models.CharField(max_length=100)
    team_member6_name        = models.CharField(max_length=100)
    team_member7_name        = models.CharField(max_length=100)
    team_member8_name        = models.CharField(max_length=100)
    internet_connectivity    = models.CharField(choices=Internet_Connectivity, max_length=20)
    one_member_details_name  = models.CharField(max_length=100)
    one_member_details_email = models.EmailField(max_length=100)
    referral_code            = models.CharField(max_length=200)

    def __str__(self):
        return self.username
