from .models import Mentor, Team, Submissions
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class MentorRegistrationForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )

    class Meta:
        model = Mentor
        fields = '__all__'


class TeamSignUpForm(forms.ModelForm):
    team_leader_phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )
    phone_number_alternate = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )

    class Meta:
        model = Team
        fields = ['team_name', 'team_leader_name', 'team_leader_emailID', 'team_leader_phone_number', 'phone_number_alternate', 'sectors_selection', 'name_of_organisation', 'is_startup', 'city_name', 'team_member2_name', 'team_member3_name', 'team_member4_name', 'team_member5_name', 'team_member6_name', 'team_member7_name', 'team_member8_name', 'alternate_member_details_name', 'alternate_member_details_email', 'referral_code']

class TeamEditForm(forms.ModelForm):
    team_leader_phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )
    phone_number_alternate = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    )

    class Meta:
        model = Team
        fields = ['team_name', 'team_leader_name', 'team_leader_emailID', 'team_leader_phone_number', 'phone_number_alternate', 'name_of_organisation', 'is_startup', 'city_name', 'team_member2_name', 'team_member3_name', 'team_member4_name', 'team_member5_name', 'team_member6_name', 'team_member7_name', 'team_member8_name', 'alternate_member_details_name', 'alternate_member_details_email', 'referral_code']


class Stage1SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['stage1_file']


class Stage2SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['stage2_file']


class Stage3SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['stage3_file']



