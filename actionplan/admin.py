from django.contrib import admin
from .models import Team, Mentor
from .forms import TeamSignUpForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Team
    add_form = TeamSignUpForm

    fieldsets = (
    *UserAdmin.fieldsets,
    (
        'Team Information',
        {
            'fields': (
                'team_name',
                'team_leader_name',
                'team_leader_emailID',
                'team_leader_phone_number',
                'phone_number_alternate',
                'college_name',
                'is_startup',
                'city_name',
                'team_member2_name',
                'team_member3_name',
                'team_member4_name',
                'team_member5_name',
                'team_member6_name',
                'team_member7_name',
                'team_member8_name',
                'internet_connectivity',
                'one_member_details_name',
                'one_member_details_email',
                'referral_code'
            )
        }
    )
    )

admin.site.register(Team, CustomUserAdmin)
admin.site.register(Mentor)
