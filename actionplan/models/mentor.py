from django.db import models
from django.utils.translation import gettext_lazy
from phonenumber_field.modelfields import PhoneNumberField

class Mentor(models.Model):

    PhoneNumber_Permissions = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    Sectors = (
        ('Women Empowerment', 'Women Empowerment'),
        ('Education and Employability','Education and Employability'),
        ('Education', 'Education'),
        ('Agriculture and Livestock', 'Agriculture and Livestock'),
        ('Heathcare', 'Heathcare'),
        ('5R-Reuse, Reduce,Recycle,Recover,Refuse', '5R-Reuse, Reduce,Recycle,Recover,Refuse'),
        ('Sustainable Energy', ' Sustainable Energy'),
        ('Pollution', 'Pollution'),
        ('Financial Inclusion and Fintech', 'Financial Inclusion and Fintech'),
        ('Water management', 'Water management'),
    )

    MentorType = (
        ('BUSINESS MENTOR', 'BUSINESS MENTOR'),
        ('TECHNICAL MENTOR', 'TECHNICAL MENTOR'),
        ('BOTH', 'BOTH'),
        )

    name                    = models.CharField(max_length=100)
    phone_number            = PhoneNumberField(null=False, blank=False, unique=True)
    city                    = models.CharField(max_length=100)
    state                   = models.CharField(max_length=100)
    current_portfolio       = models.URLField(max_length=200)
    linkedIn_ID             = models.URLField(max_length=200)
    work_timeline           = models.CharField(max_length=500)
    description             = models.TextField(gettext_lazy('description'), max_length=500, blank=True)
    phonenumber_permissions = models.CharField(choices=PhoneNumber_Permissions, max_length=200)
    sectors_selection       = models.CharField(choices=Sectors, max_length=200)
    mentor_type             = models.CharField(choices=MentorType, max_length=200)

    def __str__(self):
        return self.name
