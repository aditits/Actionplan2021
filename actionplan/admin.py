from django.contrib import admin
from .models import Team, Mentor, Submissions
from .forms import TeamSignUpForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Team
    add_form = TeamSignUpForm

    list_display = ('username', 'team_leader_emailID', 'team_leader_name', 'team_leader_phone_number')

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
                'name_of_organisation',
                'is_startup',
                'city_name',
                'team_member2_name',
                'team_member3_name',
                'team_member4_name',
                'team_member5_name',
                'team_member6_name',
                'team_member7_name',
                'team_member8_name',
                'sectors_selection',
                'alternate_member_details_name',
                'alternate_member_details_email',
                'referral_code'
            )
        }
    )
    )

class CustomSubmissions(admin.ModelAdmin):
    model = Submissions

    def team_id(self, obj):
        return obj.team.username

    def team_emailID(self, obj):
        return obj.team.team_leader_emailID

    def team_leader_name(self, obj):
        return obj.team.team_leader_name

    def team_leader_phone_number(self, obj):
        return obj.team.team_leader_phone_number


    list_display = ('stage1_file','stage2_file','team_id', 'team_emailID', 'team_leader_name', 'team_leader_phone_number')
    fieldsets = (
                    'Information',
                    {
                        'fields': ('stage1_file', 'stage2_file', 'stage3_file', 'team'),
                    }),

admin.site.register(Team, CustomUserAdmin)
admin.site.register(Mentor)
admin.site.register(Submissions, CustomSubmissions)